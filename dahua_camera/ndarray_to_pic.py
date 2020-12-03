#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '11/27/2020 19:15'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime

from PIL import Image
import numpy as np
import cv2

import matplotlib.pyplot as plt


def main():
    img = np.zeros((576, 704, 3))

    op2 = cv2.imread(r'D:\work_source\CV_Project\test_camera\WeChat Image_20201127191329.png')


    f = open(r'D:\work_source\CV_Project\test_camera\fumaliu.txt')
    row = 0
    line = 0
    # img = []
    lines = f.readlines()

    for l in lines:
        if l != '\n':
            rgb = l.replace(',\n', '').split(',')
            r = 0
            g = 0
            b = 0
            for i in rgb:
                b = int(rgb[0])
                g = int(rgb[1])
                r = int(rgb[2])
            img[row][line][0] = b
            img[row][line][1] = g
            img[row][line][2] = r
            line = line + 1
        elif l == '\n':
            line = 0
            row = row + 1
    f.close()

    img = img.astype(np.uint8)
    img0 = img[:, :, 0].astype(np.uint8)
    img1 = img[:, :, 1].astype(np.uint8)
    img2 = img[:, :, 2].astype(np.uint8)
    # im1 = Image.fromarray(img0)  # numpy 转 image类
    # im1.show()
    # im = Image.fromarray(img.,'RGB')  # numpy 转 image类
    # im.show()
    # plt.imshow(img)
    # plt.show()

    cv2.imshow('img', img)
    cv2.waitKey(100000)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
