# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-25 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_host_os_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_code', models.CharField(max_length=5)),
                ('user_name', models.CharField(max_length=50)),
                ('app_id', models.IntegerField()),
                ('app_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cmdb_app_user',
            },
        ),
    ]
