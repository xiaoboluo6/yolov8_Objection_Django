from rest_framework import serializers
from .models import ImageUpload

# 这个序列化器使得你可以将 ImageUpload 模型的实例转换为 JSON 格式，或者从 JSON 数据中创建 ImageUpload 模型的实例。
# 在使用 Django REST Framework 进行 API 开发时，序列化器是非常有用的工具，它简化了数据的处理和传输。
class ImageUploadSerializer(serializers.ModelSerializer):
    # 设置confidence_threshold字段的默认值为0.5
    confidence_threshold = serializers.FloatField(default=0.5)
    # 也可以通过form-data表单指定每个数字过滤的 confidence_threshold

    class Meta:
        model = ImageUpload
        fields = ['image_file', 'confidence_threshold']
