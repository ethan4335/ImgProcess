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
    path = r'D:\work_source\CV_Project\datasets\to_haitu\7'
    # target_file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # if '.json' in file:
            # print(os.path.splitext(file)[-1])
            # if os.path.splitext(file)[-1] is ('.JPG' or '.jpg' or '.png'):
            os.rename(os.path.join(root, file), os.path.join(root, 'rename_7_'+file))
                # target_file_list.append(os.path.join(root, file))




if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
