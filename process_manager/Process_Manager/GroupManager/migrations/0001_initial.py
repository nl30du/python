# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('grp_id', models.AutoField(primary_key=True, serialize=False)),
                ('grp_name', models.CharField(max_length=64)),
                ('c_t', models.DateTimeField()),
                ('detail', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]
