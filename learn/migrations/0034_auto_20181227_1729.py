# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-27 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0033_youtuberesource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuberesource',
            name='published_at',
            field=models.CharField(max_length=100),
        ),
    ]
