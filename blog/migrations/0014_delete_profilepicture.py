# Generated by Django 3.2.13 on 2022-08-03 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_profilepicture_user_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfilePicture',
        ),
    ]
