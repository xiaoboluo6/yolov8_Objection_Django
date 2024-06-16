# YOLOv8 检测接口
### 接口概述
该接口用于在YOLOv8模型上进行目标检测
***
### 目前只有电子秤检测
直接使用 POST请求`http://192.168.36.236:8000/yolov8/detect/demo` 

具体见下3接口列表 
***

### 基本信息
```
Base URL: http://192.168.36.236:8000/yolov8/detect
```

### 接口列表
##### 1.获取场景和模型的对应Map (hongxiang.pt TODO)
* URL: ''
* 请求方法: GET
* 描述: 获取场景名称和模型权重对应的字典
* 响应: 
```
JSON
状态码200
{
    "dict": {
        "电子秤": "dianzicheng_zbn_Test.pt",
        "烘箱": "hongxiang.pt"
    }
}
```
<br>

##### 2.根据场景更换权重设置 (这个可以不管,有默认权重,后期有两个或多个场景再使用)
* URL: '/model'
* 请求方法: POST
* 请求参数

| Key        | Type | Value                   | Description |
|:-----------|:-----|:------------------------|:------------|
| model_name | Text | dianzicheng_zbn_Test.pt | 权重文件的名称     |

* 描述: 输入权重名称 进行模型加载
* 响应:
```
JSON
状态码201
{
    "model_loaded": "dianzicheng_zbn_Test.pt"
}

状态码404
{
    "error": "没有对应的权重模型"
}  
```  
<br>

##### 3.模型检测
* URL: '/demo'
* 请求方法: POST
* 请求参数

| Key                  | Type | Value           | Description           |
|:---------------------|:-----|:----------------|:----------------------|
| image_file           | File | path_to_file    | 选择待检测文件               |
| confidence_threshold | Text | 0.5 [0.5-0.7皆可] | (非必须,建议不设置)过滤权重,默认0.5 |

* 描述: 输入权重名称 进行模型加载
* 响应:
```
状态码201
{
    "detected_result": 370.66
}

状态码500
{
    "error": "........(错误原因,反正就是检测有问题)"
}
```
<br>

##### 4.后台查看(验证模型效果,测试使用)
* 浏览器访问URL: http://192.168.36.236:8000/admin
* 描述: 查看历史检测效果
* 登录: zhangmingjian 123456

**image upload类 记录检测结果**

| 检测图 | 上传时间 | 模型名称 | 过滤字符的置信度设置 | STATUS | 图片路径 |
|:----|:-----|:-----|:-----------|:-------|:-----|

***
<br>

### 响应状态码
```
200 OK: 请求成功
201 Created: 资源创建成功
204 No Content: 请求成功，无响应体
400 Bad Request: 请求格式不正确
404 Not Found: 请求的资源不存在
500 Internal Server Error: 服务器内部错误
```  

    








