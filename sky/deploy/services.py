# -*- coding: utf-8 -*-
import os
import time
from cmdb.models import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_PATH = os.path.join(BASE_DIR, "temp")
DEPLOY_PATH = r"D:\backup\deploy"
REMOTE_DEPLOY_PATH = r"d$\backup\deploy"


# 部署时，把升级压缩包复制到对应机器
def copy_deploy_file(order_code, ip):
    host = Host.objects.filter(ip=ip)
    host_user = host.host_user
    password = host.password

    remote_path = r"\\" + ip + os.sep + REMOTE_DEPLOY_PATH
    deploy_file = os.path.join(DEPLOY_PATH, order_code, ".zip")

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
        print "复制成功"
    else:
        print "复制失败，请检查。。。"


# 主函数，测试
if __name__ =="__main__":
    order_code = "20190102144558ES"
    ip = "172.24.180.223"
    copy_deploy_file(order_code, ip)