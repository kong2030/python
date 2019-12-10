# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import os
import datetime
import shutil
# Create your tests here.


host_ip = '172.24.180.77'
program_path = r'd$\maServer'
order_code = '201912091211PD'
source_remote_path = r"\\" + host_ip + "\\" + program_path
root_program_path = program_path.split("\\")[-1]
dst_remote_path = r"\\" + host_ip + r"\d$\backup\deploy-before" + "\\" + order_code + "\\" + root_program_path


print datetime.datetime.now()
if not os.path.exists(dst_remote_path):
    # 可以忽略某些文件夹
    shutil.copytree(source_remote_path, dst_remote_path, ignore=shutil.ignore_patterns('log'))

print datetime.datetime.now()
