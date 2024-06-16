from ultralytics import YOLO

# 自定义异常
class DetectionFailedError(Exception):
    pass

class YOLOv8Detector:
    def __init__(self, model_path):
        """
        Initialize the YOLOv8 model.
        :param model_path: The path to the YOLOv8 model file (e.g., 'yolov8n.pt').
        """
        # Load the pretrained YOLOv8 model
        self.model = YOLO(model_path)

    def run_detection(self, image_path, confidence_threshold=0.42):
        """
        Run object detection on the provided image.
        :param image_path: The path to the image file.
        :return: A list of detected objects with their labels, confidence scores, and bounding boxes.
        """
        # Perform detection
        results = self.model(image_path, conf=confidence_threshold, stream=False)[0]

        # Process results
        detected_objects = []
        for det in results.boxes:  # Loop through each detection
            label_index = int(det.cls)
            label = self.model.names[label_index]
            confidence = float(det.conf)
            bbox = det.xyxy.cpu().numpy()[0]
            x_min, y_min, x_max, y_max = bbox[:4]

            detected_objects.append({
                'label': label,
                'confidence': confidence,
                'x_min': x_min,
                'y_min': y_min,
                'x_max': x_max,
                'y_max': y_max,
            })


        # 新增后处理操作
        # 这里我需要把detected_objects的检测结果进行处理 得到最终的输出结果
        # 这里会过滤掉'label' 为 'nums' 的元素
        filtered_objects = [obj for obj in detected_objects if obj['label'] != 'nums']
        # 按照 'x_min' 的值升序排序
        sorted_objects = sorted(filtered_objects, key=lambda x: x['x_min'])
        # 拼接
        detected_result = ''.join([obj['label'] for obj in sorted_objects])

        # 这里默认是两位小数,加上小数点
        try:
            detected_result = float(detected_result[:-2]+"."+detected_result[-2:])
            return detected_objects, detected_result
        except Exception as e:
            # 抛出自定义异常，并附加原始异常信息
            error_message = f"数字检测失败，原始异常信息：{str(e)}"
            raise DetectionFailedError(error_message) from e






