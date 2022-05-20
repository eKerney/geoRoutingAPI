# Generated by Django 4.0.4 on 2022-05-19 14:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convAPI', '0002_alter_surfacehex_airports_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UAVrouteInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField(null=True)),
                ('pathcost', models.FloatField(null=True)),
                ('destid', models.IntegerField(null=True)),
                ('startid', models.IntegerField(null=True)),
                ('shape_length', models.FloatField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(null=True, srid=4326)),
            ],
        ),
    ]