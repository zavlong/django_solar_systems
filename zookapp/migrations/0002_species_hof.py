# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='hof',
            field=models.CharField(default='hof', max_length=200),
            preserve_default=False,
        ),
    ]
