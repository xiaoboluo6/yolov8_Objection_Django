# Generated by Django 4.2.5 on 2023-11-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("YoloObjectDetectionAPI", "0002_alter_detections_object_detection_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="imageupload",
            name="detection_result",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="imageupload",
            name="image_file",
            field=models.ImageField(upload_to="media/images/"),
        ),
    ]
