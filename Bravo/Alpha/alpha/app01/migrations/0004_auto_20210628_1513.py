# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-06-28 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20210628_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.CharField(default='study', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.CharField(max_length=255, null=True),
        ),
    ]