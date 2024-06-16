from django.contrib import admin
from django.contrib import auth
from .models import ImageUpload, Detections
from django.utils.html import format_html

@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    # list_display = ('thumbnail', 'upload_timestamp', 'confidence_threshold', 'detected_result', 'status', 'image_file')

    # 这里改名的原因是 改名后可以用自定义的方法标签 就变成了 th
    list_display = ('thumbnail', 'formatted_upload_timestamp', 'formatted_model_name', 'confidence_threshold_center',
                    'detected_result_center', 'status', 'image_file_witdth')
    list_editable = ('status',)
    list_filter = ('status', 'upload_timestamp')    # 在右侧边栏中添加过滤器，以便用户可以通过选择特定的值来筛选模型数据
    search_fields = ('status', 'model_name')     # 用于在 admin 页面的顶部添加一个搜索框，允许用户输入关键字进行模糊搜索

    def thumbnail(self, obj):
        if obj.image_file:
            return format_html('<img src="{}" style="width: 250px; height:auto;"/>', obj.image_file.url)
        return "-"
    thumbnail.short_description = "检测图"

    # 这里新增样式修改 居中
    def confidence_threshold_center(self, obj):
        # 使用 <div> 设置样式实现居中显示
        return format_html('<div style="text-align: center;">{}</div>', obj.confidence_threshold)
    # 这里再把列名 改回来
    confidence_threshold_center.short_description = "置信度设置"

    def detected_result_center(self, obj):
        # 使用 <div> 设置样式实现居中显示
        return format_html('<div style="text-align: center;">{}</div>', obj.detected_result)
    # 这里再把列名 改回来
    detected_result_center.short_description = "检测结果"

    def image_file_witdth(self, obj):
        image_url = obj.image_file.url
        return format_html('<a href="{}" target="_blank" style="max-width: 150px; overflow: hidden; text-overflow: ellipsis; display: inline-block;">{}</a>', image_url, image_url)
    image_file_witdth.short_description = "图片路径"

    # 新增方法，格式化上传时间和模型名称的显示
    def formatted_upload_timestamp(self, obj):
        return obj.upload_timestamp.strftime("%Y-%m-%d %H:%M:%S")
    formatted_upload_timestamp.short_description = "上传时间"

    def formatted_model_name(self, obj):
        return obj.model_name
    formatted_model_name.short_description = "模型名称"

@admin.register(Detections)
class DetectionsAdmin(admin.ModelAdmin):
    list_display = ('object_detection', 'label', 'confidence', 'x_min', 'x_max', 'y_min', 'y_max', 'detection_date')
    list_filter = ('object_detection', 'label', 'detection_date')
    search_fields = ('label', 'object_detection__linked_image__image_file')
