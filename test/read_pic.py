#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '11/30/2020 18:01'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import cv2


def main():
    img = cv2.imread(r'D:\Users\Pictures\woqu.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if img is not None:
        print(len(img))


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
