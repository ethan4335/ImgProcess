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
import my_common.Files


def count_png(path,type):
    mf = my_common.Files.files()
    list1 = mf.travel_folder(path,type)
    print('png img count:',len(list1))

def main():
    path = r'D:\work_source\CV_Project\datasets\a6000\20201211\fps_interval_160'
    count_png(path,'png')


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
