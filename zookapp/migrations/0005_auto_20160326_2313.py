# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zookapp', '0004_auto_20160326_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarsystem',
            name='galaxy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='zookapp.Galaxy'),
        ),
    ]
