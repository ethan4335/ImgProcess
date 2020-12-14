#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/8/2020 17:37'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import numpy as np
import cv2


def main():
    img_path = r'D:\Users\Pictures\20201208_103400.jpg'

    img = cv2.imread(img_path)
    oh, ow, oc = img.shape
    print(oh, ow, oc)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    oh, ow, oc = img.shape
    print(oh, ow, oc)

    dh, dw, dc = np.array(np.array([oh, ow, oc]) * self.cfg.jitter, dtype=np.int)



if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
