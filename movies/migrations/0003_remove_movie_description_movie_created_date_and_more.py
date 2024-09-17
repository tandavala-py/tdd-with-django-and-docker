# Generated by Django 5.1.1 on 2024-09-17 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.AddField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
