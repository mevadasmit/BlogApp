# Generated by Django 4.2.1 on 2025-02-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_alter_postimage_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="header_image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="postimage",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]
