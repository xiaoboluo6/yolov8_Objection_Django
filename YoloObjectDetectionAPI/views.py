from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageUpload, Detections
from .serializers import ImageUploadSerializer
from .detection_models.yolov8 import YOLOv8Detector
from django.core.cache import cache

import pdb  # debug玩一下

class YoloDetectionView(APIView):
    # 默认值设置
    model_name = "dianzicheng_zbn_Test.pt"
    detector = YOLOv8Detector(model_name)
    cache.set('detector', detector)
    cache.set('model_name', model_name)

    # 返回模型dict     # "hongxiang.pt" TODO
    def get(self, request, format=None):
        mapping = {
            "电子秤": "dianzicheng_zbn_Test.pt",
            "烘箱": "hongxiang.pt"
        }
        return Response({'dict': mapping}, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        if '/demo' in request.path:
            return self.process_demo(request)
        elif '/model' in request.path:
            return self.process_model(request)
        else:
            # 正常进不来的  url锁死了
            return Response({'error': 'Invalid path for POST request'}, status=status.HTTP_400_BAD_REQUEST)

    # 测试过程
    def process_demo(self, request, format=None):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image_upload = serializer.save()

            try:
                detector = cache.get('detector')   # 从缓存中获得定义好的模型
                model_name = cache.get('model_name')
                detected_objects, detected_result = detector.run_detection(image_path=image_upload.image_file.path,confidence_threshold=image_upload.confidence_threshold)
                image_upload.status = ImageUpload.STATUS_COMPLETED
                image_upload.detected_result = detected_result
                image_upload.model_name = model_name
                image_upload.save()
            except Exception as e:
                image_upload.status = ImageUpload.STATUS_FAILED
                image_upload.save()
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # 这里我感觉其实可以存也可以不存 反正我只要输出结果
            for detection_object in detected_objects:
                Detections.objects.create(
                    object_detection=image_upload,
                    label=detection_object['label'],
                    confidence=detection_object['confidence'],
                    x_min=detection_object['x_min'],
                    x_max=detection_object['x_max'],
                    y_min=detection_object['y_min'],
                    y_max=detection_object['y_max']
                )

            # return Response({'detections': detected_objects}, status=status.HTTP_201_CREATED) # 这里是返回每一个数字的检测结果
            return Response({'detected_result': detected_result}, status=status.HTTP_201_CREATED)  # 这里返回的是经过后处理的二位小数
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 模型选择 不执行的话默认是 电子秤.pt
    def process_model(self, request, format=None):
        try:
            # 获取 form-data 中的值
            model_name = str(request.data.get('model_name', None))
            detector = YOLOv8Detector(model_name)
            # 将 detector 存入缓存
            cache.set('detector', detector)
            cache.set('model_name', model_name)
            return Response({'model_loaded': model_name}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': "没有对应的权重模型"}, status=status.HTTP_404_NOT_FOUND)