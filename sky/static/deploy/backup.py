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

# 今天日期的字符串
today_str = datetime.datetime.today().strftime("%Y%m%d")

# 当前工作目录
project_path = os.getcwd()

# 拷贝的应用根目录名字
app_name = "kcbp"

# 拷贝目录
source_path = os.path.join(r"\\172.24.180.223\d$", app_name)
base_path = r"\\172.24.180.223\d$\backup\deploy-before"


# 拷贝文件
def backup(source, dst):
    if not os.path.exists(dst):
        # 可以忽略某些文件夹
        shutil.copytree(source, dst, ignore=shutil.ignore_patterns('log'))
    else:
        print u"目录已经存在，请先整理。。。"


# 主函数
if __name__ == "__main__":
    order_code = sys.argv[1]

    des_path = os.path.join(base_path, order_code, app_name)

    
    # 备份
    backup(source_path, des_path)

    print "End Task......"
    time.sleep(2)

