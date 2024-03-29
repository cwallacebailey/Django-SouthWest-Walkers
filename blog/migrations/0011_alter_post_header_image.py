# Generated by Django 3.2.13 on 2022-07-26 15:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_post_blurb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]
