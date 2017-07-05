# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-10 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='db_info',
            fields=[
                ('db_id', models.AutoField(primary_key=True, serialize=False)),
                ('db_name', models.CharField(max_length=32)),
                ('env_id', models.IntegerField()),
                ('host_ip', models.CharField(max_length=32)),
                ('port', models.CharField(max_length=32)),
                ('host_name', models.CharField(max_length=128)),
                ('slave_db_id', models.IntegerField()),
                ('db_type', models.IntegerField()),
                ('c_t', models.DateTimeField()),
                ('manager_id', models.IntegerField()),
                ('detail', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='env',
            fields=[
                ('env_id', models.AutoField(primary_key=True, serialize=False)),
                ('env_name', models.CharField(max_length=64)),
                ('c_t', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='hosts',
            fields=[
                ('host_id', models.AutoField(primary_key=True, serialize=False)),
                ('sys_id', models.IntegerField()),
                ('host_ip', models.CharField(max_length=32)),
                ('ssh_port', models.IntegerField()),
                ('app_dir', models.CharField(max_length=64)),
                ('service_port', models.IntegerField()),
                ('env_id', models.IntegerField()),
                ('c_t', models.DateTimeField()),
            ],
        ),
    ]
