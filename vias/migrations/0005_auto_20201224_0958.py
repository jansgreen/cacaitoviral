# Generated by Django 3.1.4 on 2020-12-24 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vias', '0004_remove_vias_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vias',
            name='imagen',
        ),
        migrations.AddField(
            model_name='vias',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
