# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zookapp', '0003_auto_20160302_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]