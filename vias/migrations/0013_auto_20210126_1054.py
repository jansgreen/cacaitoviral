# Generated by Django 3.1.4 on 2021-01-26 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vias', '0012_auto_20210126_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accionesyutube',
            old_name='YoutubeUser',
            new_name='user',
        ),
    ]
