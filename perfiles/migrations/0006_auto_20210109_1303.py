# Generated by Django 3.1.4 on 2021-01-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0005_auto_20210109_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001B6AEDFC148>.png', null=True, upload_to='ImagenVia'),
        ),
    ]
