# Generated by Django 3.1.4 on 2020-12-24 01:05

import datetime
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
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_via', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_via', models.CharField(max_length=20, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
                ('imagen', models.ImageField(upload_to='ImagenVias')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vias.tipo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vias',
            },
        ),
    ]
