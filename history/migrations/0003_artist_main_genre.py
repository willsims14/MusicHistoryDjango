# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20170419_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='main_genre',
            field=models.TextField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
