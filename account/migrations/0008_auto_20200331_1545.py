# Generated by Django 3.0.4 on 2020-03-31 06:45

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200331_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(default='profile/no_image.gif', upload_to=account.models.get_uuid_profile_image_url, verbose_name='프로필 사진'),
        ),
    ]
