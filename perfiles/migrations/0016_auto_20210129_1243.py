# Generated by Django 3.1.4 on 2021-01-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0015_auto_20210129_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001A0A0021948>.png', null=True, upload_to='ImagenVia'),
        ),
    ]
