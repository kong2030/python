# -*- coding: utf-8 -*-
import os
import time
from cmdb.models import *
from deploy.models import *
import base64
import hashlib
import zipfile
import shutil

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


# 开始部署
def deploy_do(order, host):
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
    cmd_3 = os.path.join(remote_path, "deploy.py") + " " + order_code

    bat_file = os.path.join(TEMP_PATH, "temp.bat")
    with open(bat_file, "w") as f:
        print >> f, cmd_1
        print >> f, cmd_2
        print >> f, cmd_3

    time.sleep(1)
    flag = os.system(bat_file)
    if flag == 0:
        print u"发布成功"
    else:
        print u"发布失败，请检查。。。"


# 生成md5
def generate_file_md5value(file_path):
    md5 = hashlib.md5()
    # 需要使用二进制格式读取文件内容
    md5_file = open(file_path, 'rb')
    md5.update(md5_file.read())
    md5_file.close()
    return md5.hexdigest()


# md5验证，服务器端与远端发布后文件进行校验
def md5_check(order, host):
    order_code = order.order_code
    module = order.module
    program_path = module.program_path
    host_ip = host.ip
    host_user = host.host_user
    password = host.password

    # 解密
    decode_str = base64.decodestring(password)
    password = decode_str[-1] + decode_str[-2] + decode_str[2:-2] + decode_str[1] + decode_str[0]

    remote_path = r"\\" + host_ip + os.sep + program_path
    deploy_file_zip = os.path.join(DEPLOY_PATH, order_code + ".zip")

    file_unzip = zipfile.ZipFile(deploy_file_zip, 'r')
    for file_ in file_unzip.namelist():
        file_unzip.extract(file_, DEPLOY_PATH)
    # 获取解压后根目录
    app_root_dir = file_unzip.namelist()[0][:-1]
    deploy_file_path = os.path.join(DEPLOY_PATH, app_root_dir)
    # 先连接
    cmd = r"net use %s %s /user:%s" % (remote_path, password, host_user)

    md5_form_list = []
    flag = os.system(cmd)
    if flag == 0:
        remote_file_dict = {}
        for root, dirs, files in os.walk(remote_path):
            for file_ in files:
                file_path = os.path.join(root, file_)
                remote_file_dict[file_.upper()] = file_path

        for root, dirs, files in os.walk(deploy_file_path):
            for file_ in files:
                deploy_file = os.path.join(root, file_)
                md5_form = {}
                # 汇总检查结果
                result_all = 1
                md5_form["deploy_file"] = deploy_file.replace(DEPLOY_PATH + os.sep, "")
                md5_form["md5_source"] = generate_file_md5value(deploy_file)
                if file_.upper() in remote_file_dict.keys():
                    remote_file = remote_file_dict[file_.upper()]
                    md5_form["remote_file"] = remote_file
                    md5_form["md5_remote"] = generate_file_md5value(remote_file)
                    if md5_form["md5_source"] == md5_form["md5_remote"]:
                        md5_form["check_result"] = 1
                    else:
                        md5_form["check_result"] = 0
                        # 只要有一个不同就标识异常
                        result_all = 0
                    md5_form_list.append(md5_form)

    else:
        print u"连接失败，请检查。。。"

    # 删除文件
    shutil.rmtree(deploy_file_path)
    return md5_form_list, result_all


# 发布函数，对外接口
def deploy(order, host):
    copy_deploy_file(order, host)
    deploy_backup(order, host)
    deploy_do(order, host)


# 主函数，测试
if __name__ =="__main__":
    order_code = "20190102144558ES"
    ip = "172.24.180.223"
    copy_deploy_file(order_code, ip)