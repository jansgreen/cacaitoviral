# Generated by Django 3.1.4 on 2021-01-30 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vias', '0022_accionesyutube_idioma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accionesyutube',
            name='idioma',
        ),
    ]