# Generated by Django 5.1.1 on 2024-09-17 05:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_description_movie_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
