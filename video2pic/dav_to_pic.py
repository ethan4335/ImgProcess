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
import os
import time

# 抽帧，间隔时间，参照视频帧率
fps_interval = 150

input_folder = r'E:\PRIVATE\AVCHD\BDMV\STREAM'
# input_file = r'D:\Users\Desktop\video\00007.MTS'
output_folder = r'D:\work_source\CV_Project\datasets\a6000'

date = str(time.strftime("%Y-%m-%d", time.localtime())).replace('-', '')


def path_init(output=None):
    output += '\\' + date + '\\fps_interval_' + str(fps_interval)
    if not os.path.exists(output):
        os.makedirs(output)
    print('makedir: ' + output)
    return output


def read_video_file(input_file):
    video_to_pics(input_file, fps_interval)


def read_video_folder(input, output):
    for root, dirs, files in os.walk(input):
        for file in files:
            f = os.path.join(root, file)
            print('processing: ' + f)
            video_to_pics(f, fps_interval, output)


def video_to_pics(video, interval=25, output=None):
    vc = cv2.VideoCapture(video)
    c = 0
    rval = vc.isOpened()

    (path, filename) = os.path.split(video)
    video_name = str(filename).split('.')[0]
    out_path = os.path.join(output, filename)
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    while rval:
        c = c + 1
        rval, frame = vc.read()
        if rval:
            if c % interval == 0:
                cv2.imwrite(out_path + '\\' + 'zmj_' + date + '_v' + video_name + '_itv' + str(fps_interval) + '_' + str(int(c / interval)) + '.png', frame)  # 命名方式
        else:
            break
    vc.release()


def main():
    # read_video_file()

    read_video_folder(input_folder, path_init(output_folder))


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
