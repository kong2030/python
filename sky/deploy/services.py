# -*- coding: utf-8 -*-
import os
import time
import sys
from cmdb.models import *
from deploy.models import *
import base64
import hashlib
import zipfile
import shutil
import datetime
import chardet
import traceback
import logging
from stat import ST_ATIME, ST_CTIME, ST_MTIME

import cmdb.services

reload(sys)
sys.setdefaultencoding('utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_PATH = os.path.join(BASE_DIR, "temp")
DEPLOY_PATH = r"D:\backup\deploy"

# 打印日志
logger = logging.getLogger(__name__)


# 首先建立连接
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
                log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 连接存在，无需新建" + "\n"
                return flag, log_str

        # 解密
        password = cmdb.services.decrypt(password)

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
        logger.error("connection has an error:")
        logger.exception(Exception)
        flag = -1
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 连接失败，请检查:" + "\n" + str(e) + "\n"

    return flag, log_str


# 部署时，把升级压缩包复制到对应机器
def copy_deploy_file(order, host):
    try:
        host_ip = host.ip
        host_user = host.host_user
        order_code = order.order_code
        module = order.module
        program_path = module.program_path

        # 根据操作类型，升级文件的存放位置
        root_deploy_path = program_path.split("\\")[0]
        remote_path = r"\\" + host_ip + "\\" + root_deploy_path + r"\backup\deploy"
        if not os.path.exists(remote_path):
            os.makedirs(remote_path)
        deploy_file = os.path.join(DEPLOY_PATH, order_code+".zip")
        remote_path_file = os.path.join(remote_path, order_code+".zip")
        if not os.path.exists(remote_path_file):
            shutil.copy(deploy_file, remote_path)

        print u"复制成功"
        flag = 0
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 复制成功" + "\n"

    except Exception as e:
        traceback.print_exc()
        logger.error(order_code+" copy has an error:")
        logger.exception(Exception)
        flag = -1
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 复制失败，请检查:" + "\n" + str(e) + "\n"

    return flag, log_str


# 发布前在原机器上备份
def deploy_backup(order, host):
    try:
        order_code = order.order_code
        module = order.module
        program_path = module.program_path
        host_ip = host.ip

        source_remote_path = r"\\" + host_ip + "\\" + program_path
        root_program_path = program_path.split("\\")[-1]
        dst_remote_path = r"\\" + host_ip + r"\d$\backup\deploy-before" + "\\" + order_code + "\\" + root_program_path
        if not os.path.exists(dst_remote_path):
            # 可以忽略某些文件夹
            shutil.copytree(source_remote_path, dst_remote_path, ignore=shutil.ignore_patterns('log'))
        else:
            print u"目录已经存在，请先整理。。。"

        #raise RuntimeError('testError')

        print u"备份成功"
        flag = 0
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 备份成功" + "\n"
    except Exception as e:
        # 备份失败,删除备份垃圾数据
        dst_remote_path = r"\\" + host_ip + r"\d$\backup\deploy-before" + "\\" + order_code
        if os.path.exists(dst_remote_path):
            shutil.rmtree(dst_remote_path)

        traceback.print_exc()
        logger.error(order_code+" backup has an error:")
        logger.exception(Exception)
        flag = -1
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 备份失败，请检查:" + "\n" + str(e) + "\n"

    return flag, log_str


# 开始部署
def deploy_do(order, host):
    try:
        order_code = order.order_code
        module = order.module
        program_path = module.program_path
        host_ip = host.ip

        root_deploy_path = program_path.split("\\")[0]
        remote_deploy_path = r"\\" + host_ip + "\\" + root_deploy_path + r"\backup\deploy"
        remote_program_path = r"\\" + host_ip + "\\" + program_path

        # 解压到临时目录，要包含根目录
        deploy_file_zip = os.path.join(remote_deploy_path, order_code + ".zip")
        remote_deploy_path_temp = os.path.join(remote_deploy_path, str(order_code))
        if not os.path.exists(remote_deploy_path_temp):
            os.makedirs(remote_deploy_path_temp)
        f = zipfile.ZipFile(deploy_file_zip, 'r')
        # 获取解压后根目录
        app_root_dir = f.namelist()[0].split('/')[0]
        # 保留原修改时间
        for file_ in f.infolist():
            d = file_.date_time
            gettime = "%s/%s/%s %s:%s" % (d[0], d[1], d[2], d[3], d[4])
            f.extract(file_, remote_deploy_path_temp)
            file_path = os.path.join(remote_deploy_path_temp, file_.filename)
            timearry = time.mktime(time.strptime(gettime, '%Y/%m/%d %H:%M'))
            os.utime(file_path, (timearry, timearry))

        # 开始部署
        deploy_file_path = os.path.join(remote_deploy_path_temp, app_root_dir)
        cmd = r"xcopy %s %s /Y /F /E" % (deploy_file_path, remote_program_path)
        # os.system(cmd)
        result = os.popen(cmd).readlines()
        with open(os.path.join(remote_deploy_path, order_code + ".log"), "w") as f:
            for line in result:
                print >> f, line

        # md5校验
        for root,dirs,files in os.walk(deploy_file_path):
            for file_ in files:
                file_path_src = os.path.join(root, file_)
                md5_src = generate_file_md5value(file_path_src)
                file_path_dst = file_path_src.replace(deploy_file_path, remote_program_path)
                if os.path.exists(file_path_dst):
                    md5_dst = generate_file_md5value(file_path_dst)
                    if md5_src != md5_dst:
                        flag = -1
                        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 发布失败，请检查:" + "\n" + u"md5校验失败" + "\n"
                        return flag, log_str

        # 删除文件
        shutil.rmtree(remote_deploy_path_temp)

        if "复制了".encode("gb2312") in "".join(result):
            print u"发布成功"
            logger.info(order_code + u" has success flag 复制了")
            flag = 0
            log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 发布成功" + "\n"
        else:
            print u"发布失败"
            logger.info(order_code + u" has no success flag 复制了")
            flag = -1
            log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 发布失败，请检查:" + "\n" + u"没找到复制成功标志: 复制了" + "\n"

    except Exception as e:
        traceback.print_exc()
        logger.error(order_code+" deploy has an error:")
        logger.exception("EXCEPTION")
        flag = -1
        log_str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 发布失败，请检查:" + "\n" + str(e) + "\n"

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
    try:
        order_code = order.order_code
        module = order.module
        program_path = module.program_path
        host_ip = host.ip

        remote_path = r"\\" + host_ip + "\\" + program_path
        deploy_file_zip = os.path.join(DEPLOY_PATH, order_code + ".zip")
        deploy_file_zip_temp = os.path.join(DEPLOY_PATH, str(order_code))

        file_unzip = zipfile.ZipFile(deploy_file_zip, 'r')
        for file_ in file_unzip.namelist():
            file_unzip.extract(file_, deploy_file_zip_temp)
        # 获取解压后根目录
        app_root_dir = file_unzip.namelist()[0].split('/')[0]
        deploy_file_path = os.path.join(deploy_file_zip_temp, app_root_dir)

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

                    md5_form["deploy_file"] = deploy_file.replace(deploy_file_zip_temp + os.sep, "")
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
                    else:
                        md5_form["remote_file"] = "can not find the file"
                        md5_form["md5_remote"] = "has no md5"
                        md5_form["check_result"] = 0
                        # 只要有一个不同就标识异常
                        result_all = 0
                    md5_form_list.append(md5_form)

        else:
            print u"连接失败，请检查。。。"

        # 删除文件
        shutil.rmtree(deploy_file_zip_temp)
    except Exception as e:
        traceback.print_exc()
        logger.error("md5 check has an error:")
        logger.exception("EXCEPTION")

    return md5_form_list, result_all


# 发布函数，对外接口
def deploy_zip(order, host):
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


# 发布Sql
def deploy_sql(order, host):
    try:
        order_code = order.order_code
        host_ip = host.ip
        host_user = host.host_user
        password = host.password

        # 解密
        decode_str = base64.decodestring(password)
        password = decode_str[-1] + decode_str[-2] + decode_str[2:-2] + decode_str[1] + decode_str[0]

        log_str = ""
        flag = 0
        order_deploy_file_path = os.path.join(DEPLOY_PATH, str(order_code))
        for root, divs, files in os.walk(order_deploy_file_path):
            for file_ in files:
                if file_.endswith(".sql") or file_.endswith(".SQL"):
                    file_sql = os.path.join(root, file_)
                    cmd = r"sqlcmd -S %s -U %s -P %s -i %s"%(host_ip, host_user, password, file_sql.decode("gb2312"))
                    result = ".".join(os.popen(cmd.encode("gb2312")).readlines())
                    if "错误".encode("gb2312") in result or "级别".encode("gb2312") in result:
                        flag = 1
                        log_str = log_str + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + " " + file_ + "\n" + result
                        print log_str
                        break
                    else:
                        log_str = log_str + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + " " + file_ + "\n" + result
                        print log_str
    except Exception as e:
        traceback.print_exc()
        logger.error(order_code+" has an error:")
        logger.exception(Exception)
        flag = 1
        log_str = log_str + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + " " + file_ + "\n" + result

    return flag, log_str.decode("gb2312")


# 发布函数对外接口
def deploy(order, host):
    order_type = order.type
    if order_type == 1:
        flag, log_str = deploy_zip(order, host)
    else:
        flag, log_str = deploy_sql(order, host)

    return flag, log_str


# 回滚函数
def rollback(order, host):
    try:
        log_all = ""
        # 先建立连接
        flag, log_str = connect(host)
        log_all = log_all + log_str
        # 连接成功，开始回滚
        if flag == 0:
            order_code = order.order_code
            module = order.module
            program_path = module.program_path
            host_ip = host.ip

            # program_path 一般为 d$\kcbp 的值
            app_name = program_path.split("\\")[-1]
            root_deploy_path = r"\\" + host_ip + "\\" + program_path.split("\\")[0] + r"\backup\deploy"
            root_deploy_before_path = r"\\" + host_ip + "\\" + program_path.split("\\")[0] + r"\backup\deploy-before"
            program_path_all = r"\\" + host_ip + "\\" + program_path
            backup_file_order_path = os.path.join(root_deploy_before_path, order_code, app_name)
            deploy_log_file = os.path.join(root_deploy_path, order_code + ".log")

            deploy_dict = dict()
            with open(deploy_log_file, "r") as f:
                for line in f.readlines():
                    if len(line.split("->")) > 1:
                        deploy_file_has = line.split("->")[1].strip()
                        deploy_file_has_key = deploy_file_has.replace(program_path_all, "")
                        deploy_dict[deploy_file_has_key] = deploy_file_has

            count = 0
            for key, value in deploy_dict.items():
                deploy_before_file = backup_file_order_path + key
                deploy_file = value
                if os.path.exists(deploy_before_file):
                    # 回滚文件
                    shutil.copy(deploy_before_file, deploy_file)
                    # 关键步骤:保留修改时间,ST_MTIME:修改时间,ST_CTIME:文件访问时间,windows下
                    file_stat = os.stat(deploy_before_file)
                    os.utime(deploy_file, (file_stat[ST_CTIME], file_stat[ST_MTIME]))
                    # 回滚日志
                    log_all = log_all + deploy_before_file + " -> " + deploy_file + "\n"
                    count = count + 1
                else:
                    # 如果是新增的文件，直接删除文件，不过新建的空目录会被保留（影响不大就不再优化）
                    os.remove(deploy_file)
                    log_all = log_all + " delete the file: " + deploy_file + "\n"
                    count = count + 1

            log_all = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + " all rollback files: " + str(count) + "\n" + log_all

    except Exception as e:
        traceback.print_exc()
        logger.error(order_code+"rollback has an error:")
        logger.exception(Exception)
        flag = -1
        log_all = log_all + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + u" 回滚失败，请检查。。。" + "\n"

    return flag, log_all


# Sql发布
def get_order_sql_files(order_code):
    # 解压到当前目录
    deploy_file_zip = os.path.join(DEPLOY_PATH, order_code + ".zip")
    order_deploy_file_path = os.path.join(DEPLOY_PATH, str(order_code))
    if not os.path.exists(order_deploy_file_path):
        os.mkdir(order_deploy_file_path)
    file_zip = zipfile.ZipFile(deploy_file_zip, 'r')
    for file_ in file_zip.infolist():
        file_zip.extract(file_, order_deploy_file_path)

    sql_file_list = []
    for root, dirs, files in os.walk(order_deploy_file_path):
        for file_ in files:
            sql_file = os.path.join(root, file_)
            with open(sql_file, "r") as f:
                # 先读取文件内容
                sql_file_content = "".join(f.readlines())
                #print file_,chardet.detect(file_)
                #print chardet.detect(sql_file_content)
                # 只要不是 utf-8编码，一率用 gb2312 解码
                if chardet.detect(sql_file_content)["encoding"] != "utf-8" :
                    sql_file_content = sql_file_content.decode("gb2312")

                sql_file_dict = {"sql_file": file_.decode("gb2312"), "sql_file_content": sql_file_content}
                sql_file_list.append(sql_file_dict)

    # 直接把文件名与文件内容返回，免得再次解析
    return sql_file_list


# 获取order完整状态
def get_order_status_all(order_code):
    order = Order.objects.filter(order_code=order_code)[0]

    order_status_html = ""
    for env_id in range(1,6):
        env_name = Environment.objects.filter(env_id=env_id)[0].env_name
        # 使用反射获取对应环境
        arg_name = "env_" + str(env_id)
        order_status = getattr(order, arg_name)
        temp_str = ""
        if order_status == 0:
            temp_str = '<button class="btn purple">%s未发布</button>' % (env_name)
        elif order_status == 1:
            temp_str = '<button class="btn btn-primary">%s待发布</button>' % (env_name)
        elif order_status == 2:
            temp_str = '<button class="btn btn-success">%s已发布</button>' % (env_name)

        if env_id < 5:
            temp_str = temp_str + '<span class="fa fa-arrow-right"></span>'

        order_status_html = order_status_html + temp_str

    return order_status_html

# 主函数，测试
if __name__ == "__main__":
    program_path = r"d$\kcbp"
