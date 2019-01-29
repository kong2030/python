# -*- coding: utf-8 -*-
import os
import time
import sys

from models import *


# 获取用户所管系统
def get_apps_by_user(user):
    app_systems = None

    if user.is_superuser:
        # 如果是管理员，那就返回所有系统
        app_systems = AppSystem.objects.all()
    else:
        app_user_queryset = UserApp.objects.filter(user_id=user.id)
        if app_user_queryset:
            app_user = app_user_queryset[0]
            app_ids = app_user.app_id
            # 如果不为空，即表示已录入权限
            if app_ids != "":
                app_ids_list = app_ids.split(",")
                app_systems = AppSystem.objects.filter(id__in=app_ids_list)

    return app_systems
