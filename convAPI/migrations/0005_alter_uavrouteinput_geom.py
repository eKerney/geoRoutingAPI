# Generated by Django 4.0.4 on 2022-05-19 18:35

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convAPI', '0004_alter_uavrouteinput_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uavrouteinput',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(null=True, srid=4326),
        ),
    ]