# Generated by Django 5.0.4 on 2024-05-02 09:16

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0009_remove_country_id_alter_country_iso3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, spatial_index=False, srid=4326),
        ),
    ]
