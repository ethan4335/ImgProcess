#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Authon   :buf
# @Email    :niuxinzan@cennavi.com.cn
# @File     :buf_analysis.py
# Created by iFantastic on 2020/11/24


import datetime
import PIL.Image as Image
import numpy as np
import os
import sys


def main():
    sum_pic = 0
    # class_list = [0, 1, 2, 3, 4, 5, 6, 255]
    quantity_list = [0, 0, 0, 0, 0, 0, 0, 0]
    fold = r'D:\work_source\CV_Project\datasets\buf_pics'
    # fold = sys.argv[1]
    # out = sys.argv[2]
    with open('analysis.txt', 'w') as fw:
        for root, dirs, files in os.walk(fold):
            for file in files:
                img = Image.open(os.path.join(root, file))
                ary = np.array(img)
                sum_pic = sum_pic + 1
                result = [0, 0, 0, 0, 0, 0, 0]
                # 像素个数统计
                for i in range(7):
                    result[i] = np.sum(ary == i)
                # print(os.path.join(root, file),result)
                fw.write(os.path.join(root, file) + str(result) + "\n")
                # 是否含有某类像素
                for i in range(7):
                    if (ary == i).any():
                        quantity_list[i] = quantity_list[i] + 1
        # print("pic num: ", sum_pic)
        # print("class num: ", quantity_list)
        fw.write("class num: " + str(quantity_list) + "\n")


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    time_cost = end_time - start_time
    print('cost:', str(time_cost).split('.')[0])
