import sys

import numpy as np
import json
import os
import cv2
import random
import shutil

# total_map = {'ebike2_back': 0,
#              'ebike2_front': 0,
#              'ebike2_other': 0,
#              'ebike3_back': 0,
#              'ebike3_front': 0,
#              'ebike3_other': 0,
#              'ebike2_sunshade_front': 0,
#              'ebike2_sunshade_back': 0,
#              'ebike2_sunshade_other': 0,
#              'takeout_ebike2_front': 0,
#              'takeout_ebike2_back': 0,
#              'takeout_ebike2_other': 0,
#              'takeout_ebike2_sunshade_front': 0,
#              'takeout_ebike2_sunshade_back': 0,
#              'takeout_ebike2_sunshade_other': 0,
#              'takeout_ebike3_front': 0,
#              'takeout_ebike3_back': 0,
#              'takeout_ebike3_other': 0,
#              'blank': 0,
#              'head_with_helmet': 0,
#              'head_without_helmet': 0,
#              'license_moto': 0,
#              'license_ebike': 0,
#              'license_other': 0
#              }
show_map = {'ebike3_front': 'e3f',
            'ebike2_sunshade_front': 'e2sf',
            'ebike2_sunshade_back': 'e2sb',
            'takeout_ebike2_front': 'te2f',
            'takeout_ebike2_back': 'te2b',
            'takeout_ebike2_other': 'te2o',
            'takeout_ebike2_sunshade_front': 'te2sf',
            'takeout_ebike2_sunshade_back': 'te2sb',
            'takeout_ebike2_sunshade_other': 'te2so',
            'takeout_ebike3_front': 'te3f',
            'takeout_ebike3_back': 'te3b',
            'takeout_ebike3_other': 'te3o',
            'ebike3_back': 'e3b',
            'ebike2_other': 'e2o',
            'head_with_helmet': 'hwh',
            'license_moto': 'moto',
            'blank': 'blank',
            'ebike2_back': 'e2b',
            'head_without_helmet': 'hnh',
            'license_ebike': 'ebike',
            'license_other': 'other',
            'ebike3_other': 'e3o',
            'ebike2_front': 'e2f',
            'ebike2_sunshade_other': "eso"}

json_path = r"D:\work_source\CV_Project\datasets\label_check\label\6"
image_home = r"E:\org_videos\20201217_selected\selected"
img_output = r"D:\work_source\CV_Project\datasets\label_check\img_labeled\62"

img_dict = {}
for root, dirs, files in os.walk(image_home):
    for file in files:
        f = os.path.join(root, file)
        img_name = os.path.splitext(file)[0]
        img_dict[img_name] = f

if not os.path.exists(img_output):
    os.makedirs(img_output)

json_list = []
for root, dirs, files in os.walk(json_path):
    for file in files:
        f = os.path.join(root, file)
        if '无效' in f:
            continue
        json_list.append(f)
print('total json file quantity:%s' % len(json_list))

for j in json_list:
    ftt1 = open(j, 'r')
    load_dict1 = json.load(ftt1)
    j_name = os.path.basename(j)

    image_name = os.path.splitext(j_name)[0]
    # image_name = os.path.join(image_home, image_name)
    # if not os.path.exists(image_name):
    #     image_name = j.replace("json", "png")
    # if not os.path.exists(image_name):
    #     # print(image_name, "file not exist")
    #     continue
    if not image_name in img_dict.keys():
        continue

    # adding exception handling
    try:
        shutil.copy(img_dict[image_name], os.path.join(img_output,os.path.basename(img_dict[image_name])))
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())

