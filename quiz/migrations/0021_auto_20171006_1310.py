# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0020_remove_questions_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='options',
            new_name='options1',
        ),
        migrations.AddField(
            model_name='questions',
            name='options2',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='options3',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='options4',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='options5',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
