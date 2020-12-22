#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/21/2020 11:43'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import os
import json
import cv2
from shutil import copyfile

# select_labels = ['ebike3_front',
#             'ebike2_sunshade_front',
#             'ebike2_sunshade_back',
#             'takeout_ebike2_front',
#             'takeout_ebike2_back',
#             'takeout_ebike2_other',
#             'takeout_ebike2_sunshade_front',
#             'takeout_ebike2_sunshade_back',
#             'takeout_ebike2_sunshade_other',
#             'takeout_ebike3_front',
#             'takeout_ebike3_back',
#             'takeout_ebike3_other',
#             'ebike3_back',
#             'ebike2_other',
#             'head_with_helmet',
#             'license_moto',
#             'blank',
#             'ebike2_back',
#             'head_without_helmet',
#             'license_ebike',
#             'license_other',
#             'ebike3_other',
#             'ebike2_front',
#             'ebike2_sunshade_other']

label_dict = {'ebike2_front': 0,
              'ebike2_back': 1,
              'ebike2_other': 2,

              'ebike2_sunshade_front': 3,
              'ebike2_sunshade_back': 4,
              'ebike2_sunshade_other': 5,

              'ebike3_front': 6,
              'ebike3_back': 7,
              'ebike3_other': 8,

              'takeout_ebike2_front': 9,
              'takeout_ebike2_back': 10,
              'takeout_ebike2_other': 11,

              'takeout_ebike2_sunshade_front': 12,
              'takeout_ebike2_sunshade_back': 13,
              'takeout_ebike2_sunshade_other': 14,

              'takeout_ebike3_front': 15,
              'takeout_ebike3_back': 16,
              'takeout_ebike3_other': 17,
              }


# read json home to dict
def read_json_path(json_path):
    json_dict = {}
    for root, dirs, files in os.walk(json_path):
        for file in files:
            json = os.path.join(root, file)
            if 'invalid' in json:
                continue
            name = os.path.splitext(os.path.basename(json))[0]
            json_dict[name] = json
    print('total valied json file quantity: %s' % len(json_dict.keys()))
    return json_dict


# read img home to dict
def read_img_path(img_home):
    img_dict = {}
    for root, dirs, files in os.walk(img_home):
        for file in files:
            img = os.path.join(root, file)
            name = os.path.splitext(os.path.basename(img))[0]
            img_dict[name] = img
    print('total valied img quantity: %s' % len(img_dict.keys()))
    return img_dict


def convert_json_to_yolo(j_dict, i_dict, output):
    count = 0

    output_img = os.path.join(output, 'images')
    output_lbl = os.path.join(output, 'labels_yolo')
    if not os.path.exists(output_img):
        os.makedirs(output_img)
    if not os.path.exists(output_lbl):
        os.makedirs(output_lbl)

    for j in j_dict:
        json_f = j_dict[j]

        # filter empty picture
        if j in i_dict.keys():
            img = i_dict[j]
            image = cv2.imread(img)
            if image is None: continue

            copyfile(img, os.path.join(output_img, os.path.basename(img)))

            img_width, img_height = image.shape[1], image.shape[0]

            with open(json_f, encoding='utf-8') as jf:
                json_content = json.load(jf)
            shapes = json_content['shapes']
            with open(os.path.join(output_lbl, j + '.txt'), 'w') as wf:
                for each_shape in shapes:
                    # rectangle
                    if each_shape['label'] in label_dict.keys():
                        label_class = label_dict[each_shape['label']]
                        # empty rec
                        if len(each_shape['points']) < 2:
                            print(json)
                            continue
                        if len(each_shape['points'][0]) < 2:
                            print(json)
                            continue
                        x1, y1 = each_shape['points'][0][0], each_shape['points'][0][1]
                        x2, y2 = each_shape['points'][1][0], each_shape['points'][1][1]

                        x_center = ((x1 + x2) / 2) / img_width
                        y_center = ((y1 + y2) / 2) / img_height
                        width = abs(x2 - x1) / img_width
                        height = abs(y2 - y1) / img_height

                        if x_center > 1 or y_center > 1 or width > 1 or height > 1:
                            print('error json',json_f)
                            break

                        wf.write(' '.join([str(label_class), str(x_center), str(y_center), str(width), str(height)]) + '\n')
            if os.path.getsize(os.path.join(output_lbl, j + '.txt')) == 0:  # 文件大小为0
                os.remove(os.path.join(output_lbl, j + '.txt'))  # 删除这个文件
                os.remove(os.path.join(output_img, os.path.basename(img)))  # 删除对应的图片
                continue
            count = count + 1
            # if count % 100 == 0:
            #     print(str('count: %s' % count).ljust(20), str('|| img:' + os.path.basename(img)).ljust(50), str('|| label:' + os.path.basename(os.path.join(output_lbl, j + '.txt'))).ljust(50))
    print('total valied json and img: %s' % count)


def main():
    json_home = r'D:\work_source\CV_Project\datasets\label_check\label\5'
    json_home_1 = r''
    img_home = r'D:\work_source\CV_Project\datasets\label_check\img\20201211'
    img_home_1 = r'D:\work_source\CV_Project\datasets\label_check\img\20201215'
    output = r'D:\work_source\CV_Project\datasets\label_convert\5'

    if not os.path.exists(output):
        os.makedirs(output)

    json_dict = read_json_path(json_home)
    if len(json_home_1) > 0:
        json_dict.update(read_img_path(json_home_1))

    img_dict = read_img_path(img_home)
    if len(img_home_1) > 0:
        img_dict.update(read_img_path(img_home_1))
    convert_json_to_yolo(json_dict, img_dict, output)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])

#
# # 浩轩code
# def convert_to_yolo_format_1216():
#     labels_dir = '/media/wanghl/bae62e0f-e516-416b-8c1b-8b066b8eb7a7/home/qiuhx/Workspace/gaotong/data/3_label'
#     imgs_dir = labels_dir[:-6]
#     label_files = os.listdir(labels_dir)
#     for label_file in label_files:
#         with open(os.path.join(labels_dir, label_file)) as f:
#             json_content = json.load(f)
#         # img = cv2.imread(os.path.join(imgs_dir, label_file[:-4] + 'jpg'))
#         # img_width, img_height = img.shape[0], img.shape[1]
#         if 'qhx' in label_file or 'gwc' in label_file:
#             img_width, img_height = 3840, 2160
#         elif 'zmj' in label_file or 'zt' in label_file:
#             img_width, img_height = 1920, 1080
#         else:
#             print('which user?')
#         shapes = json_content['shapes']
#         with open(os.path.join(labels_dir + '_yolo', label_file[:-5] + '.txt'), 'w') as f:
#             for each_shape in shapes:
#                 # rectangle
#                 if each_shape['label'] in select_labels:
#                     #empty rec
#                     if len(each_shape['points']) < 2:
#                         print(label_file)
#                         continue
#                     if len(each_shape['points'][0]) < 2:
#                         print(label_file)
#                         continue
#                     x1, y1 = each_shape['points'][0][0], each_shape['points'][0][1]
#                     x2, y2 = each_shape['points'][1][0], each_shape['points'][1][1]
#
#                     x_center = ((x1 + x2) / 2) / img_width
#                     y_center = ((y1 + y2) / 2) / img_height
#                     width = abs(x2 - x1) / img_width
#                     height = abs(y2 - y1) / img_height
#                     f.write(
#                         ' '.join(['0', str(x_center), str(y_center), str(width), str(height)]) + '\n')
