# Generated by Django 3.1.4 on 2021-01-29 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vias', '0017_auto_20210129_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accionesyutube',
            old_name='video',
            new_name='videoURL',
        ),
    ]
