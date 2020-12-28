#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/28/2020 11:50'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import cv2
import random
import numpy as np
import json

rng = np.random.default_rng()

img = r'D:\work_source\test_env\ImgProcess\gwc_20201211_20000101_005903_190.jpg'
label = r'D:\work_source\test_env\ImgProcess\gwc_20201211_20000101_005903_190.txt'

img = cv2.imread(img)
# sp = img.shape
# height = sp[0]  # height(rows) of image
# width = sp[1]  # width(colums) of image
# sz3 = sp[2]  # the pixels value is made up of three primary colors

# read labels

def safe_float(number):
    try:
        return float(number)
    except:
        return None


label_dict=[]
labels=[]
with open(label) as lf:

    for line in lf:
        arr = line.strip("\n").split(' ')
        label_dict.append(arr)
    for s in label_dict:
        labels.append(float(s))


# for box in label_dict.values():
#     box[1] = box[1] * 1
#     box[2] = box[2] * 2
#     box[3] = box[3] * 1
#     box[4] = box[4] * 2
#     x_c, y_c, w, h = box[1], box[2], box[3], box[4]
    # print(x_c, y_c, w, h)

def gen_checkboard2(img, xywh):
    height, width = img.shape[0], img.shape[1]
    for box in xywh:
        print(box[1],width)
        # box[1] = box[1] * width
        print( box[1] * 2)
        box[2] = box[2] * height
        box[3] = box[3] * width
        box[4] = box[4] * height
        x_c, y_c, w, h = box[1], box[2], box[3], box[4]  # box x_center y_center w h pixel coordinates in image
        # cv2.rectangle(img, (int(x_c - w / 2), int(y_c - h / 2)),
        #               (int(x_c + w / 2), int(y_c + h / 2)), (0, 255, 0), 2)

        blank_area = 0.1
        blank_box_w = rng.uniform(low=0.2, high=0.8, size=1)[0]
        blank_box_h = int(blank_area / blank_box_w * h)
        blank_box_w = int(blank_box_w * w)
        blank_box_x = random.randint(int(x_c - w / 2), int(x_c + w / 2 - blank_box_w))
        blank_box_y = random.randint(int(y_c - h / 2), int(y_c + h / 2 - blank_box_h))
        blank = img[blank_box_y:blank_box_y + blank_box_h, blank_box_x:blank_box_x + blank_box_w]
        count = 0
        if 0 in blank.shape:
            #print('blank_box has 0 dimension')
            return img
        # cv2.rectangle(img, (blank_box_x, blank_box_y),
        #               (blank_box_x + blank_box_w, blank_box_y + blank_box_h),
        #               (255, 0, 255), 1)

        if random.random() < 0.7:
            # side
            side_random = random.random()
            if side_random < 0.25:
                # top
                blank_box_pos_x = random.randint(0, int(w) - blank_box_w)
                try:
                    img[int(y_c - h / 2):int(y_c - h / 2 + blank_box_h),
                    int(x_c - w / 2 + blank_box_pos_x):int(x_c - w / 2 + blank_box_pos_x + blank_box_w)] = blank
                except ValueError as err:
                    count+1
                    #print('ValueError: {0}, file:{1}'.format(err, label_file))
                # cv2.rectangle(img, (int(x_c - w / 2 + blank_box_pos_x), int(y_c - h / 2)),
                #               (int(x_c - w / 2 + blank_box_pos_x + blank_box_w), int(y_c - h / 2 + blank_box_h)),
                #               (255, 0, 0), 1)
            elif side_random < 0.5:
                # down
                blank_box_pos_x = random.randint(0, int(w) - blank_box_w)
                try:
                    img[int(y_c + h / 2 - blank_box_h):int(y_c + h / 2),
                    int(x_c - w / 2 + blank_box_pos_x):int(x_c - w / 2 + blank_box_pos_x + blank_box_w)] = blank
                except ValueError as err:
                    count+1
                    #print('ValueError: {0}, file:{1}'.format(err, label_file))
                # cv2.rectangle(img, (int(x_c - w / 2 + blank_box_pos_x), int(y_c + h / 2 - blank_box_h)),
                #               (int(x_c - w / 2 + blank_box_pos_x + blank_box_w), int(y_c + h / 2)),
                #               (255, 0, 0), 1)
            elif side_random < 0.75:
                # left
                blank_box_pos_y = random.randint(0, int(h) - blank_box_h)
                try:
                    img[int(y_c - h / 2 + blank_box_pos_y):int(y_c - h / 2 + blank_box_pos_y + blank_box_h),
                    int(x_c - w / 2):int(x_c - w / 2 + blank_box_w)] = blank
                except ValueError as err:
                    count+1
                    #print('ValueError: {0}, file:{1}'.format(err, label_file))
                # cv2.rectangle(img, (int(x_c - w / 2), int(y_c - h / 2 + blank_box_pos_y)),
                #               (int(x_c - w / 2 + blank_box_w), int(y_c - h / 2 + blank_box_pos_y + blank_box_h)),
                #               (255, 0, 0), 1)
            else:
                # right
                blank_box_pos_y = random.randint(0, int(w) - blank_box_w)
                try:
                    img[int(y_c - h / 2 + blank_box_pos_y): int(y_c - h / 2 + blank_box_pos_y + blank_box_h),
                    int(x_c + w / 2 - blank_box_w):int(x_c + w / 2)] = blank
                except ValueError as err:
                    count+1
                    #print('ValueError: {0}, file:{1}'.format(err, label_file))
                # cv2.rectangle(img, (int(x_c + w / 2 - blank_box_w), int(y_c - h / 2 + blank_box_pos_y)),
                #               (int(x_c + w / 2), int(y_c - h / 2 + blank_box_pos_y + blank_box_h)),
                #               (255, 0, 0), 1)
        else:
            # inside
            block_x1, block_y1 = random.randint(int(x_c - w / 2), int(x_c + w / 2 - blank_box_w)), \
                                 random.randint(int(y_c - h / 2), int(y_c + h / 2 - blank_box_h))
            try:
                img[int(block_y1):int(block_y1 + blank_box_h), int(block_x1): int(block_x1 + blank_box_w)] = blank
            except ValueError as err:
                    count+1
                    #print('ValueError: {0}, file:{1}'.format(err, label_file))
    return img


img2 = gen_checkboard2(img,labels)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# for label in label_dict.values():
#     img2 = gen_checkboard2(img,label)

# cv2.imshow('img2', img)


def main():
    pass


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
