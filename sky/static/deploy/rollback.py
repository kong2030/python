# -*- coding: utf-8 -*-
__author__ = 'yangwenren'
import sys
import os
import time
import shutil
import datetime
import zipfile
from stat import ST_ATIME, ST_CTIME, ST_MTIME

reload(sys)
sys.setdefaultencoding('utf8')


# 拷贝的应用根目录名字
app_name = "kcbp"

# 拷贝目录
source_path = r"\\172.24.180.223\d$\backup\deploy-before"
root_deploy_path = r"\\172.24.180.223\d$\backup\deploy"


# 发布函数
def rollback():
    # 发布单号
    order_code = "20190114093713OH"
    program_path = r"d$\kcbp"
    app_name = program_path.split("\\")[-1]
    program_path_all = r"\\172.24.180.223" + "\\" + program_path
    backup_file_order_path = os.path.join(source_path, order_code, app_name)
    deploy_log_file = os.path.join(root_deploy_path, order_code+".log")

    deploy_dict = dict()
    with open(deploy_log_file, "r") as f:
        for line in f.readlines():
            if len(line.split("->")) > 1:
                deploy_file_has = line.split("->")[1].strip()
                #print deploy_file_has
                deploy_file_has_key = deploy_file_has.replace(program_path_all,"").lower()
                #print deploy_file_has_key
                deploy_dict[deploy_file_has_key] = deploy_file_has

    log_str = ""
    count = 0
    for key, value in deploy_dict.items():
        #print key,value
        deploy_before_file = backup_file_order_path + key
        deploy_file = value
        if os.path.exists(deploy_before_file):
            shutil.copy(deploy_before_file, deploy_file)
            # 关键步骤:保留修改时间,ST_MTIME:修改时间,ST_CTIME:文件访问时间,windows下
            file_stat = os.stat(deploy_before_file)
            os.utime(deploy_file, (file_stat[ST_CTIME], file_stat[ST_MTIME]))
            log_str = log_str + deploy_before_file + " -> " + deploy_file + "\n"
            #print deploy_before_file, " -> ", deploy_file
            count = count + 1
            #cmd = r"xcopy %s %s /Y /F /E" % (deploy_before_file, deploy_file)
            #result = os.popen(cmd).readlines()
            #print "".join(result).decode("gb2312")
        else:
            print deploy_file
            shutil.rmtree(deploy_file)

    log_str = "all rollback files: " + str(count) + "\n" + log_str
    print log_str

    # 开始回退

    


# 主函数
if __name__ =="__main__":
    
    rollback()
    
    time.sleep(2)

    print "end task....."
