# Generated by Django 5.0.4 on 2024-05-03 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0012_mobility_mobilitycalendar_mobilitydone_person_result_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='mobility',
        ),
        migrations.AddField(
            model_name='mobility',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countries.institution', verbose_name='Institució'),
        ),
    ]