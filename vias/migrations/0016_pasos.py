# Generated by Django 3.1.4 on 2021-01-29 16:54

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vias', '0015_auto_20210126_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]