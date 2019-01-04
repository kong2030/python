# -*- coding: utf-8 -*-
__author__ = 'yangwenren'
import sys
import os
import time
import shutil
import datetime
import zipfile

reload(sys)
sys.setdefaultencoding('utf8')


# 拷贝的应用根目录名字
app_name = "kcbp"

# 拷贝目录
source_path = r"\\172.24.180.223\d$\backup\deploy-before"
program_path = os.path.join(r"\\172.24.180.223\d$", app_name)


# 发布函数
def rollback():
    # 发布单号
    order_code = sys.argv[1]
    backup_file_order_path = os.path.join(source_path, order_code)
    
    # 开始回退
    deploy_file_path = os.path.join(backup_file_order_path, os.listdir(backup_file_order_path)[0])
    cmd = r"xcopy %s %s /Y /F /E" % (deploy_file_path, program_path)
    os.system(cmd)
    


# 主函数
if __name__ =="__main__":
    
    rollback()
    
    time.sleep(2)
