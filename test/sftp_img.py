# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/12/10 14:59
# @Author  : xhh
# @Desc    :
# @File    : index_features.py
# @Software: PyCharm
import cv2
import os
import numpy as np
import paramiko
import urllib

# 实例化一个transport对象
transport = paramiko.Transport(('172.22.64.12', 22))
# 建立连接
transport.connect(username='lab', password='123.com')
# 实例化一个 sftp对象,指定连接的通道
sftp = paramiko.SFTPClient.from_transport(transport)
data = sftp.listdir('/APP/zmj/test_sftp/img')
print(data)
for imagename in data:
    imagepath = os.path.join('http://172.22.64.12:22/APP/zmj/test_sftp/img/', imagename)
    print(imagepath)
    resp = urllib.urlopen(imagepath)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    print(image)