# Generated by Django 4.0.4 on 2022-05-17 18:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='surfaceHex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_field', models.CharField(max_length=254)),
                ('lulc', models.CharField(max_length=254)),
                ('population', models.FloatField()),
                ('railroads', models.CharField(max_length=254)),
                ('schools', models.CharField(max_length=254)),
                ('uasfm_ceil', models.CharField(max_length=254)),
                ('h3_index', models.CharField(max_length=254)),
                ('hospitals', models.CharField(max_length=254)),
                ('prisons', models.CharField(max_length=254)),
                ('fcc_asr', models.CharField(max_length=254)),
                ('roads', models.CharField(max_length=254)),
                ('transmissi', models.CharField(max_length=254)),
                ('helipads', models.CharField(max_length=254)),
                ('stadium', models.CharField(max_length=254)),
                ('electric_s', models.CharField(max_length=254)),
                ('police_sta', models.CharField(max_length=254)),
                ('eocs', models.CharField(max_length=254)),
                ('airports', models.CharField(max_length=254)),
                ('wind_farms', models.CharField(max_length=254)),
                ('uasfm_max', models.FloatField()),
                ('uasfm_min', models.FloatField()),
                ('score', models.FloatField()),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
