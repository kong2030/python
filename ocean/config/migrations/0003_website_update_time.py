# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-13 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='update_time',
            field=models.DateTimeField(null=True),
        ),
    ]
