# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_auto_20171005_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
