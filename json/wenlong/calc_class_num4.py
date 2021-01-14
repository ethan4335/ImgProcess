import numpy as np
import glob
import time
import os
import json
import time

all_path = []
def getallfile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath=os.path.join(path,file)
        if 'invalid' in filepath:continue
        if os.path.isdir(filepath):
            getallfile(filepath)
        elif os.path.isfile(filepath):
            if 'json' in filepath:
                all_path.append(filepath)

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
              'license_other': 0,
              'moto_front': 0,
              'moto_back': 0,
              'moto_other': 0
              }

label_home = os.getcwd()
getallfile(label_home)
time_now = time.strftime("%Y%m%d-%H%M", time.localtime())

haitu_path = []
ours_path = []

txtpath = os.path.join(label_home, time_now+".txt")

total_num = len(all_path)
for path in all_path:
    ftt1 = open(path, 'r')
    load_dict1 = json.load(ftt1)
    for target in load_dict1['shapes']:
        if target['label'] not in label_dict:
            print ("wrong label!~ ", path)
            print(target['label'])
            continue
        label_dict[target['label']]+=1
total_box_num = 0

for key,v in label_dict.items():
    total_box_num += v

# for home, dirs, files in os.walk(label_home):
#     for dir in dirs:
#         paths = glob.glob(os.path.join(os.path.join(home,dir), '*.json'))
#         total_num += len(paths)
#         for path in paths:
#             ftt1 = open(path, 'r')
#             load_dict1 = json.load(ftt1)
#             for target in load_dict1['shapes']:
#                 if target['label'] not in label_dict:
#                     print ("wrong label!~ ", path)
#                     continue
#                 label_dict[target['label']]+=1

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


