# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-23 02:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0009_auto_20190122_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='modes',
        ),
    ]
