#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '12/2/2020 10:05'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import os


def main():
    files = os.walk(r'C:\Users\Ethan\WebDownload\LiveRecord\video_1_pic_d25')
    for path, dir_list, file_list in files:
        for file_name in file_list:
            os.rename(os.path.join(path, file_name), os.path.join(path, 'v1_' + file_name))


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
