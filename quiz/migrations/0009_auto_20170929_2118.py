# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20170929_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contests',
            name='duration',
        ),
        migrations.AddField(
            model_name='contests',
            name='d_day',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='contests',
            name='d_hour',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='contests',
            name='d_minute',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
