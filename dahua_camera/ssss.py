#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Authon   :buf
# @Email    :niuxinzan@cennavi.com.cn
# @File     :ssss.py
# Created by iFantastic on 2020/11/27

import cv2
import  numpy as np
if __name__ == '__main__':
    sss=cv2.imread('d:/data/111.png')
    b = sss[:,:,0]
    g = sss[:,:,1]
    r = sss[:,:,2]
    nnn = np.zeros_like(sss)
    nnn[:,:,0]=r
    nnn[:,:,1]=g
    nnn[:,:,2]=b

    cv2.imshow('sss',nnn)
    cv2.waitKey(100000)