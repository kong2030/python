# -*- coding: utf-8 -*-
import datetime
import os
import sys
import chardet
import codecs
import traceback
import logging
import json
import time
from stat import ST_ATIME, ST_CTIME, ST_MTIME

from cmdb.models import *
import cmdb.services

reload(sys)
sys.setdefaultencoding('utf-8')

# 初始化日志实例，使用默认
logging = logging.getLogger()


# 大日志切割，按时间
def cut_log_qq_kcbp(log_file, time_str, interval, output_path, date_str="1900-01-01"):
    try:
        file_name = os.path.basename(log_file)
        output_file_name = "cut_" + file_name
        output_file = open(os.path.join(output_path, output_file_name), "w")

        datetime_str = date_str + " " + time_str
        datetime_begin = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        datetime_end = datetime_begin + datetime.timedelta(seconds=interval)

        log_1000 = ""
        count = 0
        if date_str == "1900-01-01":
            datetime_begin_str = datetime_begin.strftime("%Y%m%d%H%M%S")[8:]
            datetime_end_str = datetime_end.strftime("%Y%m%d%H%M%S")[8:]

            with open(log_file, "r") as f:
                for line in f:
                    log_time_str = line[10:16]
                    if line.startswith("["):
                        if log_time_str > datetime_end_str:
                            break
                        elif log_time_str >= datetime_begin_str:
                            count = count + 1
                            if count <= 100:
                                log_1000 = log_1000 + line

                            print >> output_file, line,

                    else:
                        continue

            if count == 0:
                log_1000 = "has no records match !!!!!!!!!! \n"
        else:
            datetime_begin_str = datetime_begin.strftime("%Y%m%d-%H%M%S")
            datetime_end_str = datetime_end.strftime("%Y%m%d-%H%M%S")

            with open(log_file, "r") as f:
                for line in f:
                    log_time_str = line[1:16]
                    if line.startswith("["):
                        if log_time_str > datetime_end_str:
                            break
                        elif log_time_str >= datetime_begin_str:
                            count = count + 1
                            if count <= 100:
                                log_1000 = log_1000 + line

                            print >> output_file, line,

                    else:
                        continue

            if count == 0:
                log_1000 = "has no records match !!!!!!!!!! \n"

        return log_1000, count

    except Exception as e:
        # traceback.print_exc()
        logging.error(e)
        #logging.exception(Exception)
        return str(e), -1


# 大日志搜索，按关键字，qq_kcbp
def search_log_qq_kcbp(log_file, keyword, output_path):
    try:
        file_name = os.path.basename(log_file)
        output_file_name = "search_" + file_name
        output_file = open(os.path.join(output_path, output_file_name), "w")

        # 先获取 msgid
        with open(log_file, "r") as f:
            line_key = ""
            msg = ""
            msg_key_set = set()
            for line in f:
                if line_key != line[:50]:
                    if keyword.encode("gb2312") in msg:
                        index = msg.find("MsgId=")
                        if index != -1:
                            msg_key_set.add(msg[index+6:index+30])
                    line_key = line[:50]
                    msg = line
                else:
                    msg = msg + line

            print msg_key_set

        # 转换为 headid
        with open(log_file, "r") as f:
            header_key_set = set()
            for line in f:
                for msg_key in msg_key_set:
                    if msg_key in line:
                        header_key_set.add(line[:50])
                        break

        # 取所有 headid 相同的行
        count = 0
        log_1000 = ""
        with open(log_file, "r") as f:
            for line in f:
                if line[:50] in header_key_set:
                    count = count + 1
                    if count <= 100:
                        log_1000 = log_1000 + line
                    print >> output_file, line,

        if count == 0:
            log_1000 = "has no records match !!!!!!!!!!"


        return log_1000, count
    except Exception as e:
        #traceback.print_exc()
        logging.error(e)
        #logging.exception(Exception)
        return str(e), -1


# 大日志搜索，按关键字，qq_bpu
def search_log_qq_bpu(log_file, keyword, output_path):
    try:
        file_name = os.path.basename(log_file)
        output_file_name = "search_" + file_name
        output_file = open(os.path.join(output_path, output_file_name), "w")

        # 先获取 msgid
        # 头部长度
        header_length = 55
        with open(log_file, "r") as f:
            line_key = ""
            msg = ""
            msg_key_set = set()
            for line in f:
                if line_key != line[:header_length]:
                    if keyword.encode("gb2312") in msg:
                        index = msg.find("msgid=")
                        if index != -1:
                            msg_key_set.add(msg[index+6:index+30])
                    line_key = line[:header_length]
                    msg = line
                else:
                    msg = msg + line

            print msg_key_set

        # 转换为 headid
        with open(log_file, "r") as f:
            header_key_set = set()
            for line in f:
                for msg_key in msg_key_set:
                    if msg_key in line:
                        header_key_set.add(line[:header_length])
                        break

        # 取所有 headid 相同的行
        count = 0
        log_1000 = ""
        with open(log_file, "r") as f:
            for line in f:
                if line[:header_length] in header_key_set:
                    count = count + 1
                    if count <= 100:
                        log_1000 = log_1000 + line
                    print >> output_file, line,

        if count == 0:
            log_1000 = "has no records match !!!!!!!!!! \n"


        return log_1000, count
    except Exception as e:
        #traceback.print_exc()
        logging.error(e)
        #logging.exception(Exception)
        return str(e), -1


# 切割日志，对外
def cut_log(log_type,log_file, time_str, interval, output_path, date_str="1900-01-01"):
    log_1000 = ""
    count = 0
    if log_type == "qq_kcbp":
        log_1000, count = cut_log_qq_kcbp(log_file, time_str, interval, output_path, date_str)
    elif log_type == "qq_bpu":
        log_1000, count = cut_log_qq_kcbp(log_file, time_str, interval, output_path, date_str)
    return log_1000, count


# 搜索日志，对外
def search_log(log_type,log_file, keyword, output_path):
    log_1000 = ""
    count = 0
    if log_type == "qq_kcbp":
        log_1000, count = search_log_qq_kcbp(log_file, keyword, output_path)
    elif log_type == "qq_bpu":
        log_1000, count = search_log_qq_bpu(log_file, keyword, output_path)
    return log_1000, count


# 截取远程主机的日志
def cut_log_by_host_qq_kcbp(host,log_path, datetime_str, interval, output_path):
    try:
        flag, log_str = cmdb.services.connect(host)
        log_1000 = ""
        count = 0
        if flag == 0:
            output_file_name = host.ip + "_cut_runlog.log"
            output_file = open(os.path.join(output_path, output_file_name), "w")

            datetime_begin = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
            datetime_end = datetime_begin + datetime.timedelta(seconds=interval)

            datetime_begin_str = datetime_begin.strftime("%Y%m%d-%H%M%S")
            datetime_end_str = datetime_end.strftime("%Y%m%d-%H%M%S")

            date_str = datetime_begin_str[:8]

            log_path_date = os.path.join(r"\\", host.ip, log_path, date_str)
            if os.path.exists(log_path_date):
                for root, dirs, files in os.walk(log_path_date):
                    for file_ in files:
                        file_path = os.path.join(root, file_)
                        file_stat = os.stat(file_path)
                        log_file_ctime = time.strftime("%Y%m%d-%H%M%S", time.localtime(file_stat[ST_CTIME]))
                        log_file_mtime = time.strftime("%Y%m%d-%H%M%S", time.localtime(file_stat[ST_MTIME]))

                        if log_file_mtime >= datetime_begin_str and datetime_begin_str >= log_file_ctime:
                            with open(file_path, "r") as f:
                                for line in f:
                                    log_time_str = line[1:16]
                                    if line.startswith("["):
                                        if log_time_str > datetime_end_str:
                                            break
                                        elif log_time_str >= datetime_begin_str:
                                            count = count + 1
                                            if count <= 100:
                                                log_1000 = log_1000 + line

                                            print >> output_file, line,

                                    else:
                                        continue

                        if count == 0:
                            log_1000 = "has no records match !!!!!!!!!! \n"
            else:
                log_1000 = "do not has the log directory !!!!!!!!! \n"
                count = -1

        else:
            log_1000 = log_str
            count = -1

        return log_1000, count

    except Exception as e:
        return str(e), -1


# 切割日志接口（远程）
def cut_log_remote(log_type, host, log_path, datetime_str, interval, output_path):
    log_1000 = ""
    count = 0
    if log_type == "qq_kcbp":
        log_1000, count = cut_log_by_host_qq_kcbp(host, log_path, datetime_str, interval, output_path)
    elif log_type == "qq_bpu":
        log_1000, count = cut_log_by_host_qq_kcbp(host, log_path, datetime_str, interval, output_path)
    return log_1000, count



if __name__ == '__main__':
    print datetime.datetime.now()

    #cut_log(log_file, time_str, interval)

    #search_log(log_file, keyword)

    print datetime.datetime.now()