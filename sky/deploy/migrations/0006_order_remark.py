# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-09 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0005_auto_20190103_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='remark',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
