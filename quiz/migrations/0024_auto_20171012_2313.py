# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0023_auto_20171008_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='contests',
            name='prizes',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='rules',
            field=models.CharField(max_length=1000),
        ),
    ]
