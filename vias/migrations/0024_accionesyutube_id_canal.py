# Generated by Django 3.1.4 on 2021-02-14 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vias', '0023_remove_accionesyutube_idioma'),
    ]

    operations = [
        migrations.AddField(
            model_name='accionesyutube',
            name='Id_Canal',
            field=models.CharField(max_length=355, null=True),
        ),
    ]