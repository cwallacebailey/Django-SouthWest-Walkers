# Generated by Django 3.2.13 on 2022-08-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_post_post_blurb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='notes',
            field=models.TextField(max_length=150, null=True),
        ),
    ]
