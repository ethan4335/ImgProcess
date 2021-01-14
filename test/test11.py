#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '1/14/2021 18:07'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import os


def main():
    print(os.path.splitext(r"D:\work_source\CV_Project\datasets\label_check\6\00000_261.png")[0])


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
