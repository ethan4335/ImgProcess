#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '11/26/2020 9:42'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import os
import filetype


class files():
    def __init__(self):
        # self.path = path
        # self.type = type
        pass

    # 这个是样例
    def read_txt(self, file):
        f = open(file)
        line = f.readline()
        while line:
            print(line)
            print(type(line))
            line = f.readline()
        f.close()

    # 这个是样例
    def write_txt(self, file):
        folder = os.path.abspath(os.path.dirname(os.getcwd()))  # 获取上级目录
        # os.path.abspath(os.path.join(os.getcwd(), "..")) # 获取上级目录
        # os.path.abspath(os.path.join(os.getcwd(), "../..")) #获取上上级目录
        if not os.path.exists(folder):
            os.makedirs(folder)

        with open(file, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write("I am Meringue.\n")
            f.write("I am now studying in NJTECH.\n")

    # 遍历文件夹
    def travel_folder(self, path, type):
        path = str(path)
        type = str(type)
        target_file_list = []
        for root, dirs, files in os.walk(path):
            for file in files:
                f = os.path.join(root, file)
                # 啥类型都要
                if type is '*':
                    target_file_list.append(f)
                else:
                    kind = filetype.guess(f)
                    if kind is None:
                        continue
                    # print('File extension: %s' % kind.extension)
                    if kind.extension is type:
                        target_file_list.append(f)

        return target_file_list
