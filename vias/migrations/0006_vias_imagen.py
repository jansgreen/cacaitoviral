# Generated by Django 3.1.4 on 2020-12-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vias', '0005_auto_20201224_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='vias',
            name='imagen',
            field=models.ImageField(null=True, upload_to='ImagenVia'),
        ),
    ]
