# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 承销商 model
class Underwriter(models.Model):
    underwriter = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)


# 打新产品 model
class Product(models.Model):
    product_code = models.CharField(max_length=50)
    record_code = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50)
    sz_account = models.CharField(max_length=50, null=True, blank=True)
    sh_account = models.CharField(max_length=50, null=True, blank=True)
    bank_account = models.CharField(max_length=256, null=True, blank=True)