# Generated by Django 3.0.6 on 2020-05-21 20:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('cd_geocodm', models.CharField(max_length=20)),
                ('nm_municip', models.CharField(max_length=60)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='SaoPaulo',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('uf', models.CharField(max_length=254)),
                ('nome', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Incidences',
            },
        ),
    ]