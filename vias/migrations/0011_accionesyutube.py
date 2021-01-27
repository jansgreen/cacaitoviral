# Generated by Django 3.1.4 on 2021-01-25 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vias', '0010_auto_20201226_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccionesYutube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_ID', models.CharField(max_length=355, null=True)),
                ('Titulo', models.CharField(max_length=355, null=True)),
                ('comentar', models.IntegerField(default=0, null=True)),
                ('reproducion', models.BooleanField(default=False)),
                ('compartir', models.IntegerField(default=0, null=True)),
                ('Me_Gusta', models.IntegerField(default=0, null=True)),
                ('Suscripcion', models.IntegerField(default=0, null=True)),
                ('YoutubeUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Acciones',
            },
        ),
    ]