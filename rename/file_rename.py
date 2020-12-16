#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/14/2020 11:32'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
# import my_common.Files
import os

'''
00004_22250
zmj_20201211_v00007_itv160_2
'''


def main():
    path = r'D:\work_source\CV_Project\datasets\a6000\20201211\fps_interval_160\00006.MTS_zmj_filtered_labeled'

    target_file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            target_file_list.append(os.path.join(root, file))

    for f in target_file_list:
        name = os.path.basename(f)
        video = name.split('.')[0].split('_')[0]
        type = name.split('.')[1]
        count = int(int(name.split('.')[0].split('_')[1]) / 5)
        new_name = 'zmj_20201211_v' + video + '_itv160_' + str(count)+'.'+type
        os.rename(os.path.join(path, name), os.path.join(path, new_name))


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
