# Generated by Django 3.1.4 on 2021-01-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vias', '0021_auto_20210129_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='accionesyutube',
            name='idioma',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
