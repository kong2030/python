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
source_path = r"\\172.24.180.223\d$\backup\deploy"
program_path = os.path.join(r"\\172.24.180.223\d$", app_name)


# 发布函数
def deploy():
    # 发布单号
    order_code = sys.argv[1]
    # 解压到当前目录，要包含根目录
    deploy_file_zip = os.path.join(source_path, order_code+".zip")
    f = zipfile.ZipFile(deploy_file_zip,'r')
    #for file in f.namelist():       
     #   f.extract(file,source_path)
    # 获取解压后根目录
    app_root_dir = f.namelist()[0][:-1]
    # 保留原修改时间
    for file in f.infolist():
        d = file.date_time
        gettime = "%s/%s/%s %s:%s" % (d[0], d[1], d[2], d[3], d[4])
        f.extract(file, source_path)
        filep = os.path.join(source_path, file.filename)
        timearry = time.mktime(time.strptime(gettime, '%Y/%m/%d %H:%M'))
        os.utime(filep, (timearry, timearry))
    
    # 开始部署
    deploy_file_path = os.path.join(source_path, app_root_dir)
    cmd = r"xcopy %s %s /Y /F /E" % (deploy_file_path, program_path)
    #os.system(cmd)
    result = os.popen(cmd).readlines()
    with open(os.path.join(source_path,order_code+".log"), "w") as f:
        for line in result:
            print >> f, line
    # 删除文件
    shutil.rmtree(deploy_file_path)


# 主函数
if __name__ =="__main__":
    
    deploy()
    
    time.sleep(2)
