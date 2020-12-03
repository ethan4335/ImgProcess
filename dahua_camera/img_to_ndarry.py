#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '11/27/2020 19:32'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime

from PIL import Image
import numpy as np


def main():
    im = Image.open(r"D:\work_source\CV_Project\test_camera\WeChat Image_20201127191329.png")
    # im.show()
    img = np.array(im)  # image类 转 numpy
    # print(len(img))
    img = img[:, :, 1]  # 第1通道
    im = Image.fromarray(img)  # numpy 转 image类
    im.show()


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
