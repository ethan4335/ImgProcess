#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/14/2020 10:34'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import os
import time

time_now = time.strftime("%Y%m%d-%H%M", time.localtime())
file_home = os.getcwd()
print(file_home)
txtpath = os.path.join(file_home, 'check_repetition_'+time_now+".txt")
print(txtpath)

def check_repetition(path_home):
    names = set()
    with open(txtpath, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        # f.write("test\n")
        for root, dirs, files in os.walk(path_home):
            for file in files:
                # f = os.path.join(root, file)
                # if type in file:
                if file in names: f.write(os.path.join(root, file)+"\n")
                else: names.add(file)
    f.close()

check_repetition(file_home)
