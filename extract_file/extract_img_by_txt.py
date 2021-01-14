import sys

# import json
import os
import shutil


# show_map = {'ebike3_front': 'e3f',
#             'ebike2_sunshade_front': 'e2sf',
#             'ebike2_sunshade_back': 'e2sb',
#             'takeout_ebike2_front': 'te2f',
#             'takeout_ebike2_back': 'te2b',
#             'takeout_ebike2_other': 'te2o',
#             'takeout_ebike2_sunshade_front': 'te2sf',
#             'takeout_ebike2_sunshade_back': 'te2sb',
#             'takeout_ebike2_sunshade_other': 'te2so',
#             'takeout_ebike3_front': 'te3f',
#             'takeout_ebike3_back': 'te3b',
#             'takeout_ebike3_other': 'te3o',
#             'ebike3_back': 'e3b',
#             'ebike2_other': 'e2o',
#             'head_with_helmet': 'hwh',
#             'license_moto': 'moto',
#             'blank': 'blank',
#             'ebike2_back': 'e2b',
#             'head_without_helmet': 'hnh',
#             'license_ebike': 'ebike',
#             'license_other': 'other',
#             'ebike3_other': 'e3o',
#             'ebike2_front': 'e2f',
#             'ebike2_sunshade_other': "eso"}

# json_path = r"D:\work_source\CV_Project\datasets\labels_original\7_val"
# image_home = r"D:\work_source\CV_Project\datasets\to_haitu_img\7"
# img_output = r"D:\work_source\CV_Project\datasets\to_haitu_img\7_val"
def extract(txt_path,image_home,img_output):
    img_dict = {}

    for root, dirs, files in os.walk(image_home):
        for file in files:
            f = os.path.join(root, file)
            img_name = os.path.splitext(file)[0]
            img_dict[img_name] = f

    img_output_list = []
    if os.path.exists(img_output):
        for root, dirs, files in os.walk(img_output):
            for file in files:
                f = os.path.join(root, file)
                img_name = os.path.splitext(file)[0]
                img_output_list.append(img_name)

    if not os.path.exists(img_output):
        os.makedirs(img_output)

    txt_list = []
    for root, dirs, files in os.walk(txt_path):
        for file in files:
            f = os.path.join(root, file)
            if 'txt' not in f:
                continue
            txt_list.append(f)
    print('total txt file quantity:%s' % len(txt_list))

    for j in txt_list:
        j_name = os.path.basename(j)

        image_name = os.path.splitext(j_name)[0]

        if not image_name in img_dict.keys():
            continue

        # adding exception handling
        try:
            if image_name not in img_output_list:
                shutil.copy(img_dict[image_name], os.path.join(img_output,os.path.basename(img_dict[image_name])))
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())

