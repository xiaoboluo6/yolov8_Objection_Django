from django.urls import path
from .views import YoloDetectionView

urlpatterns = [
    path('detect/demo', YoloDetectionView.as_view(), name='yolov8-detection'),    # 模型检测
    path('detect/model', YoloDetectionView.as_view(), name='yolov8-detection'),   # 模型权重设置
    path('detect', YoloDetectionView.as_view(), name='yolov8-detection'),         # 返回有哪些模型权重,即对应的权重
]
