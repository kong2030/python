# -*- coding: utf-8 -*-
import os
import time
import sys
import datetime
import base64
import traceback
import logging

from models import *


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


# 建立主机连接
def connect(host):
    try:
        host_ip = host.ip
        host_user = host.host_user
        password = host.password

        # 判断连接是否已经存在
        result = os.popen("net use").readlines()
        for line in result:
            if "OK" in line.upper() and host_ip in line:
                flag = 0
                log_str = u"已经存在连接，无需再新建"
                print log_str
                return flag, log_str

        # 解密
        password = decrypt(password)

        # 根据操作类型，升级文件的存放位置
        os_id = host.os_type.os_id
        if os_id == 1:
            remote_path = r"\\" + host_ip + os.sep + "d$"
        else:
            remote_path = r"\\" + host_ip + os.sep + host_user

        cmd = r"net use %s %s /user:%s" % (remote_path, password, host_user)

        flag = os.system(cmd)
        log_str = ""
        if flag == 0:
            print u"连接成功"
            log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 连接成功" + "\n"
        else:
            print u"连接失败，请检查。。。"
            log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 连接失败，请检查。。。" + "\n"

    except Exception as e:
        traceback.print_exc()
        logging.error("connection has an error:")
        logging.exception(Exception)
        flag = -1
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 连接失败，请检查。。。" + "\n"

    return flag, log_str


# 加密，返回加密串
def encrypt(plaintext):
    temp = plaintext[-1] + plaintext[-2] + plaintext[2:-2] + plaintext[1] + plaintext[0]
    ciphertext = base64.encodestring(temp)
    return ciphertext


# 解密，返回解密串
def decrypt(ciphertext):
    temp = base64.decodestring(ciphertext)
    plaintext = temp[-1] + temp[-2] + temp[2:-2] + temp[1] + temp[0]
    return plaintext

