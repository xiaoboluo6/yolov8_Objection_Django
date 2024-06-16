# 使用方法
***
##### 接口运行
```
python manage.py runserver 192.168.36.236:8000
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
