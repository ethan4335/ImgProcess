#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '11/30/2020 19:56'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import sys


def main():
    print('Argument List:', str(sys.argv))
    print('Argument List:', str(sys.argv[1]))


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
