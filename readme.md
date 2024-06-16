# 代码说明

## 数据集

数据集生成改于 OCR 文字数据集生成模型 SynthText  
SynthText 源代码链接：[ankush-me/SynthText](https://github.com/ankush-me/SynthText)  
电子秤数据集生成链接：**后续补充 TODO**

## YOLOv8 Django 部署

源代码链接：[sezer-muhammed/Django-Yolov8-API-App](https://github.com/sezer-muhammed/Django-Yolov8-API-App)

## 使用方法

### 环境部署

```sh
# Create a new conda environment
conda create -n yolov8Django python=3.8

# Activate the environment
conda activate yolov8Django

# Install PyTorch (adjust the command based on your system specifics)
conda install ...

# Install other required packages
pip install -r requirements.txt
```

### 代码运行
```sh
# 数据库迁移
python manage.py migrate

# 创建超级用户，后续访问admin页面
python manage.py createsuperuser  
python manage.py runserver

```
















***
##### 后台审查   
##### 帐号 zhangmingjian 密码 123456
```
浏览器    http://192.168.36.236:8000/admin
```
***
##### 返回对应场景的模型权重名称
```
GET请求   http://192.168.36.236:8000/yolov8/detect
```
***
##### 针对场景设置模型
```
POST请求  http://192.168.36.236:8000/yolov8/detect/model

form-data示例    model_name:dianzicheng_zbn_Test.pt
```
***
##### 传入图片(置信度可以不传,默认0.5) 进行检测
##### 如果不设置模型 默认就是电子秤.pt 直接可以进行检测
```
POST请求   http://192.168.36.236:8000/yolov8/detect/demo

form-data示例    image_file:  选择file类型的文件
                confidence_threshold:0.5 [这个可以不写]    
```
***
