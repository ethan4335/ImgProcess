#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/14/2020 15:06'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import matplotlib as plt
from PIL import Image
from PIL import ImageEnhance
import my_common.Files
import numpy as np
import cv2 as cv
import os



# 遮挡
def paint(imagepath,x1,y1,x2,y2,output):
    img = Image.open(imagepath)
    ary = np.array(img)
    # print(ary.shape)
    img1 = ary[:, :, 0]  # 第1通道
    img2 = ary[:, :, 1]  # 第1通道
    img3 = ary[:, :, 2]  # 第1通道

    # print(ary.shape[0]) # 高 1080
    # print(ary.shape[1]) # 宽 1920
    # print(ary.shape[2]) # 通道

    for i in range(0, ary.shape[0]):
        for j in range(0, ary.shape[1]):
            if  x2 == x1 and i<x1:
                img1[i, j] = 0
                img2[i, j] = 0
                img3[i, j] = 0
            if x2 != x1 and j < int((i-x1)*(y2-y1)/(x2-x1))+y1:
            # if i> 50 and j > 1150:
                img1[i, j] = 0
                img2[i, j] = 0
                img3[i, j] = 0

    c = np.dstack((img1, img2))
    c = np.dstack((c, img3))

    im = Image.fromarray(c)  # numpy 转 image类
    # im.show()
    # output = os.path.abspath(imagepath) + '_paint'
    imgname = os.path.basename(imagepath).replace('.png','_paint.jpg')


    im.save(os.path.join(output,imgname),quality=100)

def main():
    folder = r'D:\work_source\CV_Project\datasets\a6000\20201215\fps_interval_45\b00002.MTS'
    output= r'D:\work_source\CV_Project\datasets\a6000\20201215\fps_interval_45_paint'

    if not os.path.exists(output):
        os.makedirs(output)

    mf = my_common.Files.files()
    list_f = mf.travel_folder(folder)
    print(len(list_f))
    list_json = mf.travel_folder_type_name(folder,'json')
    c = 0
    for f in list_f:
        if 'paint' in f:
            continue
        if 'json' in f:
            continue
        paint(f, 220, 192, 220, 1784,output)
        c += 1
        print(c)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
