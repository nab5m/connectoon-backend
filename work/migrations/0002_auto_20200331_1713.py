# Generated by Django 3.0.4 on 2020-03-31 08:13

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import work.models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='work.Work')),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=work.models.get_uuid_artwork_image_url), size=None, verbose_name='작품_이미지')),
            ],
            options={
                'verbose_name': '작화',
                'verbose_name_plural': '작화',
            },
            bases=('work.work',),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='work.Work')),
                ('content', models.TextField(verbose_name='스토리 본문')),
            ],
            options={
                'verbose_name': '스토리',
                'verbose_name_plural': '스토리',
            },
            bases=('work.work',),
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': '작품', 'verbose_name_plural': '작품'},
        ),
    ]
