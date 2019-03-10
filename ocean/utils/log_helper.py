# -*- coding: utf-8 -*-
import datetime
import os
import chardet
import codecs


# 大日志切割
def cut_log_qq_kcbp(log_file, time_str, interval, output_path=r"C:\Users\guosen\Desktop\output"):
    date_str = "2019-03-08"
    datetime_str = date_str + " " + time_str
    datetime_begin = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    datetime_end = datetime_begin + datetime.timedelta(minutes=interval)
    datetime_begin_str = datetime_begin.strftime("%Y%m%d%H%M%S")[8:]
    datetime_end_str = datetime_end.strftime("%Y%m%d%H%M%S")[8:]

    file_name = os.path.basename(log_file)
    output_file_name = "cut_" + file_name
    output_file = open(os.path.join(output_path, output_file_name), "w")

    log_1000 = ""
    with open(log_file, "r") as f:
        count = 0
        for line in f:
            log_time_str = line[10:16]

            if line.startswith("["):
                if log_time_str > datetime_end_str:
                    break
                elif log_time_str > datetime_begin_str:
                    count = count + 1
                    if count <= 100:
                        log_1000 = log_1000 + line + "<br>"

                    print >> output_file, line,

            else:
                continue
    print "count:", count
    return log_1000


# 大日志搜索
def search_log_qq_kcbp(log_file, keyword, output_path=r"C:\Users\guosen\Desktop\output"):
    file_name = os.path.basename(log_file)
    output_file_name = "search_" + file_name
    output_file = open(os.path.join(output_path, output_file_name), "w")

    with open(log_file, "r") as f:
        line_key = ""
        msg = ""
        msg_key_set = set()
        for line in f:
            if line_key != line[:50]:
                if keyword in msg:
                    index = msg.find("MsgId=")
                    if index != -1:
                        msg_key_set.add(msg[index+6:index+30])
                line_key = line[:50]
                msg = line
            else:
                msg = msg + line

        print msg_key_set

    with open(log_file, "r") as f:
        header_key_set = set()
        for line in f:
            for msg_key in msg_key_set:
                if msg_key in line:
                    header_key_set.add(line[:50])
                    break

    count = 0
    with open(log_file, "r") as f:
        for line in f:
            if line[:50] in header_key_set:
                count = count + 1
                print >> output_file, line,

    print "count:", count


# 切割日志，对外
def cut_log(log_type,log_file, time_str, interval):
    if log_type == "qq_kcbp":
        log_1000 = cut_log_qq_kcbp(log_file, time_str, interval)
        return log_1000


# 搜索日志，对外
def search_log(log_type,log_file, keyword):
    if log_type == "qq_kcbp":
        search_log_qq_kcbp(log_file, keyword)


if __name__ == '__main__':
    print datetime.datetime.now()

    #cut_log(log_file, time_str, interval)

    #search_log(log_file, keyword)

    print datetime.datetime.now()