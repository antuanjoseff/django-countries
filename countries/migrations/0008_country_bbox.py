# Generated by Django 5.0.4 on 2024-04-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0007_alter_country_options_alter_institution_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='bbox',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]