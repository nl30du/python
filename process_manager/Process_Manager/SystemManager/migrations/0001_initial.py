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
            name='project',
            fields=[
                ('pjt_id', models.AutoField(primary_key=True, serialize=False)),
                ('sys_id', models.IntegerField()),
                ('project_name', models.CharField(max_length=64)),
                ('git_addr', models.CharField(max_length=128)),
                ('db_id', models.IntegerField()),
                ('c_t', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='sys',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('sys_name', models.CharField(max_length=64)),
                ('owner_id', models.IntegerField()),
                ('pd_id', models.IntegerField()),
                ('c_t', models.DateTimeField()),
            ],
        ),
    ]
