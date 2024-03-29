# Generated by Django 3.2.13 on 2022-08-03 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepicture',
            name='profile_image_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='auth.user'),
            preserve_default=False,
        ),
    ]
