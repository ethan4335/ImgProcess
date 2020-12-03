#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '11/25/2020 10:51'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from shutil import copyfile

'''
把云事业部的标注文件和图片对应起来
'''
import datetime
import os

from my_common.Files import files


def main():
    json_folder = r'D:\work_source\CV_Project\datasets\dataresult'
    pic_folder = r'D:\work_source\CV_Project\datasets\待标定_20201111'
    new_pic_folder = r'D:\work_source\CV_Project\datasets\xi_an_20201125'

    fs = files()

    json_list = fs.travel_folder(json_folder, '*')
    print("json file num: %s" % len(json_list))

    json_name_list = []
    for file in json_list:
        json_name_list.append(os.path.basename(file).replace('.json', ''))

    if not os.path.exists(new_pic_folder):
        os.makedirs(new_pic_folder)
    pic_list = fs.travel_folder(pic_folder, 'jpg')
    print("pic file num: %s" % len(pic_list))

    for pic in pic_list:
        # pic_name = pic.split('\\')[len(pic.split('\\')) - 1]
        pic_name = os.path.basename(pic).replace('.jpg', '')
        if pic_name in json_name_list:
            new_file = new_pic_folder + '/' + pic_name + '.jpg'
            print(new_file)
            copyfile(pic, new_file)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('time cost: %s' %str(datetime.datetime.now() - start_time).split('.')[0])
