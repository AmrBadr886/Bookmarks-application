# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(),
        ),
    ]