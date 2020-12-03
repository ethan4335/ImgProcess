#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '11/11/2020 14:34'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import cv2
import os


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print('mkdir:', path)


'''
图片旋转
'''


def rotate(image, angle, center=None, scale=1.0):  # 1
    (h, w) = image.shape[:2]  # 2
    if center is None:  # 3
        center = (w // 2, h // 2)  # 4

    M = cv2.getRotationMatrix2D(center, angle, scale)  # 5

    rotated = cv2.warpAffine(image, M, (w, h))  # 6
    return rotated  # 7


def video2pic(file, out_path, frequency, name):
    mkdir(out_path)
    vc = cv2.VideoCapture(file)
    c = 1
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        rval, frame = vc.read()
        if c % frequency == 0:
            if frame is not None:
                # cv2.imwrite(file.replace('.MOV', '/') + str(c) + '.jpg', frame)
                # frame = rotate(frame,-90) #图片旋转一下哦
                cv2.imwrite(out_path + '/' + name + '_' + str(c) + '.jpg', frame)
                print(c)
        c = c + 1
        cv2.waitKey(1)
    vc.release()


def main():
    # video2pic(r'C:\Users\Ethan\WebDownload\LiveRecord\20000101_002735.dav','C:\\Users\\Ethan\\WebDownload\\LiveRecord\\video_1_pic_d25',25,'p')
    g = os.walk(r'H:\非机动车执法自采数据\所有视频\90')
    out = r'D:\work_source\CV_Project\dataset\footbridge_2020-11-11\video2pic2'
    for path, dir_list, file_list in g:
        for file_name in file_list:
            name = file_name.split('.')[0]
            file = os.path.join(path, file_name)
            print(file)
            video2pic(file, out + '/' + name, 60, name)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print(str(end_time - start_time).split('.')[0])
