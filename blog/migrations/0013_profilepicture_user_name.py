# Generated by Django 3.2.13 on 2022-08-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepicture',
            name='user_name',
            field=models.CharField(default=25, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]