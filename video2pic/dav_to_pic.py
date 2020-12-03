#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '12/1/2020 10:06'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import cv2


def main():
    vc = cv2.VideoCapture(r'C:\Users\Ethan\WebDownload\LiveRecord\20000101_011238.dav')
    c = 0
    rval = vc.isOpened()

    while rval:
        c = c + 1
        rval, frame = vc.read()
        if rval:
            if c % 25 == 0:
                cv2.imwrite('C:\\Users\\Ethan\\WebDownload\\LiveRecord\\video_2_pic_d25\\v2_' + str(c) + '.jpg', frame)  # 命名方式
        else:
            break
    vc.release()


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
