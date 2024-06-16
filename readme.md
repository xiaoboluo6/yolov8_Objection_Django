# 代码说明

## 数据集

数据集生成改于 OCR 文字数据集生成模型 SynthText  
SynthText 源代码链接：[ankush-me/SynthText](https://github.com/ankush-me/SynthText)  
电子秤数据集生成链接：**后续补充 TODO**

## 部署

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

# 运行
python manage.py runserver
```

## API说明
详见Api.pdf

## 模型权重


