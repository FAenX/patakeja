# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161004_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keja',
            old_name='position',
            new_name='_geolocation',
        ),
    ]
