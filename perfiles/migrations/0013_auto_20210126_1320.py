# Generated by Django 3.1.4 on 2021-01-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0012_auto_20210126_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000002146D94F548>.png', null=True, upload_to='ImagenVia'),
        ),
    ]