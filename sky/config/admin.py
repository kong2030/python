# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from . import models

# Register your models here.


# Define an inline admin descriptor for user model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = models.UserInfo
    can_delete = False
    verbose_name_plural = 'addition'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


