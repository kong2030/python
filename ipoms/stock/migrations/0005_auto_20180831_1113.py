# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
