# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_auto_20170927_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_admin',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Contests'),
        ),
    ]
