#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/25/2020 17:46'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import json
import os

label_dict = {'ebike2_front': 0,
              'ebike2_back': 0,
              'ebike2_other': 0,
              'ebike2_sunshade_front': 0,
              'ebike2_sunshade_back': 0,
              'ebike2_sunshade_other': 0,
              'ebike3_front': 0,
              'ebike3_back': 0,
              'ebike3_other': 0,
              'takeout_ebike2_front': 0,
              'takeout_ebike2_back': 0,
              'takeout_ebike2_other': 0,
              'takeout_ebike2_sunshade_front': 0,
              'takeout_ebike2_sunshade_back': 0,
              'takeout_ebike2_sunshade_other': 0,
              'takeout_ebike3_front': 0,
              'takeout_ebike3_back': 0,
              'takeout_ebike3_other': 0,
              'blank': 0,
              'head_with_helmet': 0,
              'head_without_helmet': 0,
              'license_ebike': 0,
              'license_moto': 0,
              'license_other': 0
              }

json_path = r"D:\work_source\CV_Project\datasets\label_check\label\6"
txtpath = json_path + '.txt'

json_list = []
for root, dirs, files in os.walk(json_path):
    for file in files:
        f = os.path.join(root, file)
        if '无效' in f:
            continue
        json_list.append(f)
print('total json file quantity:%s' % len(json_list))


total_num = len(json_list)
for j in json_list:
    with open(j, encoding='utf-8') as jf:
        load_dict1 = json.load(jf)

        for target in load_dict1['shapes']:
            if target['label'] not in label_dict:
                print ("wrong label!~ ", j)
                print(target['label'])
                continue
            label_dict[target['label']]+=1
    total_box_num = 0

for key,v in label_dict.items():
    total_box_num += v

with open(txtpath, 'w') as fw:
    print("total num = ",total_num)
    print("total_box_num = ",total_box_num)
    print("="*64)
    fw.write("total box num = " + str(total_box_num) + "\n")
    fw.write("total num = " + str(total_num) + "\n")
    fw.write("="*64)
    fw.write('\n')
    for key,v in label_dict.items():
        print('%-30s : %d'%(key,v))
        #fw.write(key+" : "+ str(v) +'\n')
        fw.write('%-30s : %d \n'%(key,v))
