# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-03 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0008_auto_20180627_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmdtrack',
            name='logintype',
            field=models.IntegerField(default=0),
        ),
    ]