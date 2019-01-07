# -*- coding: utf-8 -*-
import os
import time
from cmdb.models import *
from deploy.models import *
import base64
import hashlib
import zipfile
import shutil
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_PATH = os.path.join(BASE_DIR, "temp")
DEPLOY_PATH = r"D:\backup\deploy"


# 首先建立连接
def connect(host):
    host_ip = host.ip
    host_user = host.host_user
    password = host.password

    # 解密
    decode_str = base64.decodestring(password)
    password = decode_str[-1] + decode_str[-2] + decode_str[2:-2] + decode_str[1] + decode_str[0]

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

    return flag, log_str


# 部署时，把升级压缩包复制到对应机器
def copy_deploy_file(order, host):
    host_ip = host.ip
    host_user = host.host_user
    order_code = order.order_code

    # 根据操作类型，升级文件的存放位置
    os_id = host.os_type.os_id
    if os_id == 1:
        remote_deploy_path = r"d$\backup\deploy"
    else:
        remote_deploy_path = os.path.join(host_user, "backup", "deploy")

    remote_path = r"\\" + host_ip + os.sep + remote_deploy_path
    deploy_file = os.path.join(DEPLOY_PATH, order_code+".zip")

    cmd = r"xcopy %s %s /Y" % (deploy_file, remote_path)

    time.sleep(1)
    flag = os.system(cmd)
    log_str = ""
    if flag == 0:
        print u"复制成功"
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 复制成功" + "\n"
    else:
        print u"复制失败，请检查。。。"
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 复制失败，请检查。。。" + "\n"

    return flag, log_str


# 发布前在原机器上备份
def deploy_backup(order, host):
    order_code = order.order_code
    module = order.module
    module_name = module.module_name
    script_path = module.script_path
    host_ip = host.ip

    remote_path = r"\\" + host_ip + os.sep + script_path

    cmd = os.path.join(remote_path, "backup.py") + " " + order_code

    time.sleep(1)
    flag = os.system(cmd)
    log_str = ""
    if flag == 0:
        print u"备份成功"
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 备份成功" + "\n"
    else:
        print u"备份失败，请检查。。。"
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 备份失败，请检查。。。" + "\n"

    return flag, log_str


# 开始部署
def deploy_do(order, host):
    order_code = order.order_code
    module = order.module
    script_path = module.script_path
    host_ip = host.ip

    remote_path = r"\\" + host_ip + os.sep + script_path

    cmd = os.path.join(remote_path, "deploy.py") + " " + order_code

    time.sleep(1)
    flag = os.system(cmd)
    log_str = ""
    if flag == 0:
        print u"发布成功"
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 发布成功" + "\n"
    else:
        print u"发布失败，请检查。。。"
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 发布失败，请检查。。。" + "\n"

    return flag, log_str


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

    remote_path = r"\\" + host_ip + os.sep + program_path
    deploy_file_zip = os.path.join(DEPLOY_PATH, order_code + ".zip")

    file_unzip = zipfile.ZipFile(deploy_file_zip, 'r')
    for file_ in file_unzip.namelist():
        file_unzip.extract(file_, DEPLOY_PATH)
    # 获取解压后根目录
    app_root_dir = file_unzip.namelist()[0][:-1]
    deploy_file_path = os.path.join(DEPLOY_PATH, app_root_dir)

    # 先建立连接
    flag, log_str = connect(host)

    md5_form_list = []
    if flag == 0:
        remote_file_dict = {}
        for root, dirs, files in os.walk(remote_path):
            for file_ in files:
                file_path = os.path.join(root, file_)
                # 保证文件路径也是一样的，防止同名
                key = file_path.replace(remote_path, "").upper()
                remote_file_dict[key] = file_path

        # 汇总检查结果，1：表示检查无不同
        result_all = 1
        for root, dirs, files in os.walk(deploy_file_path):
            for file_ in files:
                deploy_file = os.path.join(root, file_)
                # 保证文件路径也是一样的，防止同名
                key = deploy_file.replace(deploy_file_path, "").upper()
                md5_form = dict()

                md5_form["deploy_file"] = deploy_file.replace(DEPLOY_PATH + os.sep, "")
                md5_form["md5_source"] = generate_file_md5value(deploy_file)
                if key in remote_file_dict.keys():
                    remote_file = remote_file_dict[key]
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
    log_all = ""
    # 先建立连接
    flag, log_str = connect(host)
    log_all = log_all + log_str
    if flag == 0:
        # 1：复制升级文件到对应机器
        flag, log_str = copy_deploy_file(order, host)
        log_all = log_all + log_str
        if flag == 0:
            # 2：全量备份程序
            flag, log_str = deploy_backup(order, host)
            log_all = log_all + log_str
            if flag == 0:
                # 3：开始部署
                flag, log_str = deploy_do(order, host)
                log_all = log_all + log_str

    # 返回：标记和日志
    return flag, log_all


# 主函数，测试
if __name__ == "__main__":
    order_code = "20190102144558ES"
    ip = "172.24.180.223"
    copy_deploy_file(order_code, ip)