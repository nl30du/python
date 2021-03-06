# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-10 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='db_backup_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('db_id', models.CharField(max_length=64)),
                ('day_of_week', models.CharField(max_length=64)),
                ('hour', models.CharField(max_length=64)),
                ('minute', models.CharField(max_length=64)),
                ('status', models.IntegerField()),
                ('is_running', models.IntegerField()),
                ('shell_dir', models.CharField(max_length=128)),
            ],
        ),
    ]
