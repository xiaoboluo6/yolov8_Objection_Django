## Introduction
改写文字识别数据生成模型Synthtext，模拟数码管数字图片，解决数据集少，人工标注复杂的问题  
针对现实场景中数码管阴影残留，仪器检测位数和实际值不统一的问题，调整数据生成的方式  
在上述生成数据集和真实工业场景进行目标检测训练，实现测试数据的检测  
利用Django框架部署检测模型，编写API文档提供服务调用  

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

# 运行
python manage.py runserver
```

## 模型权重

模型权重文件已上传至百度网盘，可以通过以下链接下载：

**下载链接**:[百度网盘](https://pan.baidu.com/s/1aKUqTtYL5_u6JppCR6mrtQ)  |  **提取码**:`xbl6`

请将下载的权重文件直接放置到当前目录下。

## API说明
详见 [Api.pdf](./Api.pdf)或[Api.md](./Api.md)




# Other Links

## 数据集与部署

- SynthText 源代码链接：[`ankush-me/SynthText`](https://github.com/ankush-me/SynthText)  
- 电子秤数据集生成链接：**后续补充 TODO**
- 部署源代码链接：[`sezer-muhammed/Django-Yolov8-API-App`](https://github.com/sezer-muhammed/Django-Yolov8-API-App)





