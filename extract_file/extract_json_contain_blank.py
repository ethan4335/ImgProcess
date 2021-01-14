import sys

import json
import os
import shutil


json_path = r"D:\work_source\CV_Project\datasets\labels_original\7_val"
json_out = r'D:\work_source\test_env_py\add_blank_area\json_contain_blank'

if not os.path.exists(json_out):
    os.makedirs(json_out)


# root 原始根目录
# dirs 子文件夹名字
# files 文件名list
for root, dirs, files in os.walk(json_path):
    for file in files:
        f = os.path.join(root, file)
        json_content = json.load(open(f, 'r'))
        shapes = json_content['shapes']
        for each_shape in shapes:
            if each_shape['label'] == 'blank':
                # 复制一份文件
                if os.path.basename(f) in os.listdir(json_out): continue
                print(f)
                shutil.copy(f, os.path.join(json_out, os.path.basename(f)))



