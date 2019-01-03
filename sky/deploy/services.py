# -*- coding: utf-8 -*-
import os
import time
from cmdb.models import *
from deploy.models import *
import base64

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_PATH = os.path.join(BASE_DIR, "temp")
DEPLOY_PATH = r"D:\backup\deploy"
REMOTE_DEPLOY_PATH = r"d$\backup\deploy"


# 部署时，把升级压缩包复制到对应机器
def copy_deploy_file(order, host):
    host_ip = host.ip
    host_user = host.host_user
    password = host.password
    order_code = order.order_code

    # 解密
    decode_str = base64.decodestring(password)
    password = decode_str[-1] + decode_str[-2] + decode_str[2:-2] + decode_str[1] + decode_str[0]

    remote_path = r"\\" + host_ip + os.sep + REMOTE_DEPLOY_PATH
    deploy_file = os.path.join(DEPLOY_PATH, order_code+".zip")

    cmd_1 = r"@echo off"
    cmd_2 = r"net use %s %s /user:%s" % (remote_path, password, host_user)
    cmd_3 = r"xcopy %s %s /Y /F /E" % (deploy_file, remote_path)

    bat_file = os.path.join(TEMP_PATH, "temp.bat")
    with open(bat_file, "w") as f:
        print >> f, cmd_1
        print >> f, cmd_2
        print >> f, cmd_3

    time.sleep(1)
    flag = os.system(bat_file)
    if flag == 0:
        print u"复制成功"
    else:
        print u"复制失败，请检查。。。"


# 发布前在原机器上备份
def deploy_backup(order, host):
    order_code = order.order_code
    module = order.module
    module_name = module.module_name
    script_path = module.script_path
    host_ip = host.ip
    host_user = host.host_user
    password = host.password

    # 解密
    decode_str = base64.decodestring(password)
    password = decode_str[-1] + decode_str[-2] + decode_str[2:-2] + decode_str[1] + decode_str[0]

    remote_path = r"\\" + host_ip + os.sep + script_path

    cmd_1 = r"@echo off"
    cmd_2 = r"net use %s %s /user:%s" % (remote_path, password, host_user)
    cmd_3 = os.path.join(remote_path, "backup.py") + " " + order_code

    bat_file = os.path.join(TEMP_PATH, "temp.bat")
    with open(bat_file, "w") as f:
        print >> f, cmd_1
        print >> f, cmd_2
        print >> f, cmd_3

    time.sleep(1)
    flag = os.system(bat_file)
    if flag == 0:
        print u"备份成功"
    else:
        print u"备份失败，请检查。。。"


# 发布函数
def deploy(order, host):
    #copy_deploy_file(order, host)
    deploy_backup(order, host)


# 主函数，测试
if __name__ =="__main__":
    order_code = "20190102144558ES"
    ip = "172.24.180.223"
    copy_deploy_file(order_code, ip)