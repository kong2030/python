# -*- coding: utf-8 -*-
import os
import time
import sys

from models import *
import base64


# 获取用户所管系统
def get_apps_by_user(user):
    # 默认是无结果，只不过需要保持这种数据结构
    app_systems = AppSystem.objects.filter(id=-1)

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


# 加密
def encrypt(password):
    temp = password[-1] + password[-2] + password[2:-2] + password[1] + password[0]
    encrypt_str = base64.encodestring(temp)
    return encrypt_str


# 解密，返回解密串
def decrypt(ciphertext):
    temp = base64.decodestring(ciphertext)
    plaintext = temp[-1] + temp[-2] + temp[2:-2] + temp[1] + temp[0]
    return plaintext
