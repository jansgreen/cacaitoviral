# Generated by Django 3.1.4 on 2021-01-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0010_auto_20210126_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(default='<django.db.models.query_utils.DeferredAttribute object at 0x00000267F935F588>.png', null=True, upload_to='ImagenVia'),
        ),
    ]
