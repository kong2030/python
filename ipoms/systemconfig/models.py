# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 扩展user表
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    telephone = models.CharField(max_length=16, null=True, blank=True)  ##固定电话
    mobilephone = models.CharField(max_length=11, null=True, blank=True)  ##手机

