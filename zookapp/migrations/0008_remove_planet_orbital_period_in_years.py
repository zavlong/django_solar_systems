# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 03:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zookapp', '0007_galaxy_reference_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planet',
            name='orbital_period_in_years',
        ),
    ]