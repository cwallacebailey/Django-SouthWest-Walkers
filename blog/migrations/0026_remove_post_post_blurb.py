# Generated by Django 3.2.13 on 2022-08-17 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_blurb',
        ),
    ]
