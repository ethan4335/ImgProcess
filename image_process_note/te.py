#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/28/2020 14:28'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import cv2
import random

def main():
    img = r'D:\work_source\test_env\ImgProcess\gwc_20201211_20000101_005903_190.jpg'
    label = r'D:\work_source\test_env\ImgProcess\gwc_20201211_20000101_005903_190.txt'

    img = cv2.imread(img)


    cv2.imwrite('D:/work_source/test_env/ImgProcess/test_out/' + str(random.randint(1,10000))+'.png', img)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
