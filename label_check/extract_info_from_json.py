# -*- coding: utf-8 -*-
'''
@Time          : 2020/05/08 11:45
@Author        : Tianxiaomo
@File          : coco_annotatin.py
@Noice         :
@Modificattion :
    @Author    :
    @Time      :
    @Detail    :

'''
import json
import os
import sys

# sys.argv[1]
'''
分训练集和验证集，先 3：7 开吧'''

"""hyper parameters"""
# input
ni_json_folder = r'D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\label'
# pic_folder = 'D:/work_source/CV_Project/datasets/xi_an_20201125/train/pic'

# output
# total_jspn_file = r'D:\work_source\CV_Project\datasets\xi_an_20201125\train\annotations_xi_an_20201125.csv'
# all_name_file = r'D:\work_source\CV_Project\datasets\xi_an_20201125\train\names_xi_an_20201125.csv'
all_name_cn_file = r'D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\names.csv'
# output dict
# dict_output_path = 'D:/work_source/CV_Project/datasets/xi_an_20201125/train/dict_xi_an.txt'

# if len(sys.argv)>0:
#     ni_json_folder = sys.argv[1]
#     pic_folder = sys.argv[2]
#
#     total_jspn_file = sys.argv[3]
#     all_name_file = sys.argv[4]
#     all_name_cn_file = sys.argv[5]
#     dict_output_path = sys.argv[6]


# read navinfo json file
annotations = []
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
name_set = set()  # 类别
name_set_cn = {}

file_quantity = 0
for fn in os.listdir(ni_json_folder):
    file_quantity += 1
print("file_quantity: %s" % file_quantity)

# file_quantity_70 = int(file_quantity * 0.7)
# print("file_quantity_70: %s" % file_quantity_70)

# 生成一个字典文件给模型训练使用，因为在前馈环节需要一个tensor独有量，这个字典给后面的get img id 使用
img_dict = {}
f_code_dict = {}
dict_name_shape = {}

file_num = 0
for root, dirs, files in os.walk(ni_json_folder):
    for file in files:
        file_json = os.path.join(root, file)
        file_num = file_num + 1
        with open(file_json, encoding='utf-8') as f:
            # img_name = os.path.basename(file_json).replace('.json', '') + '.jpg'
            data = json.load(f)
            annotation_new = []
            objects = data['shapes']
            # have_target = False
            # annotation_new.append(pic_folder + '/' + str(img_name))
            for obj in objects:
                label_name = obj['label']
                shape_type = obj['shape_type']
                # f_code = obj['f_code']
                # f_code_index = 0
                if label_name not in dict_name_shape.keys():
                    dict_name_shape[label_name] = shape_type
                # else:
                #     len1 = len(f_code_dict)
                #     f_code_dict[label_name] = len1
                # f_name = obj['f_name']
                # name_set_cn[str(label_name)] = f_name
            #     name_set.add(f_code)
            #     for point in obj_points:
            #         if 'w' in point:
            #             have_target = True
            #             w = point['w']
            #             x = point['x']
            #             h = point['h']
            #             y = point['y']
            #             x1 = int(x)
            #             y1 = int(y)
            #             x2 = x1 + int(w)
            #             y2 = y1 + int(h)
            #             obj_new = str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + str(f_code_dict[f_code])
            #             annotation_new.append(obj_new)
            #
            # # write one pic annotation to file
            # ana_str = ''
            # if have_target:
            #     for ana in annotation_new:
            #         ana_str = ana_str + str(ana) + ' '
            #     annotations.append(ana_str)

            # if have_target is not True:
            #     try:
            #         os.remove(os.path.join(pic_folder, img_name))
            #     except:
            #         pass
            # dict
            # img_dict[img_name] = '{:012d}'.format(file_num - 1)

# print(len(annotations))
# with open(total_jspn_file, 'w', encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
#     for line in annotations:
#         f.write(str(line.strip()).replace('\'', '') + '\n')
#         # f.newlines()
#
# with open(all_name_file, 'w', encoding='utf-8') as f:
#     for line in name_set:
#         f.write(str(line) + '\n')

with open(all_name_cn_file, 'w', encoding='utf-8') as f:
    for name in dict_name_shape.keys():
        f.write("\'"+name + "\'"+ ':'+"\'"+dict_name_shape[name]+ "\'" +','+ '\n')

"""把图片字典输出到文件"""
# with open(dict_output_path, 'w') as dict_f:
#     for d in img_dict:
#         dict_f.write(d + '-' + img_dict[d] + '\n')
