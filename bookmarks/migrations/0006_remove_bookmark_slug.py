# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0005_auto_20160423_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='slug',
        ),
    ]