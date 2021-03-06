# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-15 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.CharField(max_length=16)),
                ('clock', models.DateTimeField()),
                ('item', models.CharField(max_length=50)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OptOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trd_date', models.CharField(max_length=8)),
                ('order_date', models.CharField(max_length=8)),
                ('order_time', models.DateTimeField()),
                ('order_id', models.CharField(max_length=20)),
                ('order_status', models.CharField(max_length=1)),
                ('int_org', models.CharField(max_length=8)),
                ('cust_code', models.BigIntegerField()),
                ('cust_name', models.CharField(max_length=100)),
                ('cuacct_code', models.BigIntegerField()),
                ('stkex', models.CharField(max_length=1)),
                ('stkbd', models.CharField(max_length=2)),
                ('stkpbu', models.CharField(max_length=8)),
                ('trdacct', models.CharField(max_length=20)),
                ('subacct_code', models.CharField(max_length=8)),
                ('stk_biz', models.IntegerField()),
                ('stk_biz_action', models.IntegerField()),
                ('stk_biz_ex', models.CharField(max_length=8)),
                ('opt_num', models.CharField(max_length=16)),
                ('channel', models.CharField(max_length=1)),
            ],
        ),
    ]
