# Generated by Django 3.1.4 on 2021-01-07 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001A4F5FD7B88>.png', null=True, upload_to='ImagenVia')),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('Direccion', models.CharField(max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
