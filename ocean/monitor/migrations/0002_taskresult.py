# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-18 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField()),
                ('task_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_run_time', models.DateTimeField(blank=True, null=True)),
                ('operator', models.CharField(blank=True, max_length=255, null=True)),
                ('threshold', models.IntegerField(blank=True, null=True)),
                ('sql_result', models.IntegerField(blank=True, null=True)),
                ('monitor_result', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
