import numpy as np
import json
import os
import cv2
import random

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

json_path = r"D:\work_source\CV_Project\datasets\yolov5_test\json"
image_home = r"D:\work_source\CV_Project\datasets\yolov5_test\images"
img_output = r"D:\work_source\test_env\ImgProcess\abeled"

# read all original image
img_dict = {}
for root, dirs, files in os.walk(image_home):
    for file in files:
        f = os.path.join(root, file)
        img_name = os.path.splitext(file)[0]
        img_dict[img_name] = f


# print(os.path.basename(img))
# print(os.path.abspath(img))
# print(os.path.dirname(img))
# print()



if not os.path.exists(img_output):
    os.makedirs(img_output)

rate = 1

total = 0
show_h = np.int32(720 * 1.3)
show_w = np.int32(1280 * 1.3)
# show_h = 1
# show_w = 1

json_list = []
for root, dirs, files in os.walk(json_path):
    for file in files:
        f = os.path.join(root, file)
        if '无效' in f:
            continue
        json_list.append(f)
print('total json file quantity:%s' % len(json_list))
print('sample rate:%s' % rate)
json_random_selected = random.sample(json_list, int(len(json_list) * rate))
print('selected json file quantity:%s' % len(json_random_selected))

for j in json_random_selected:
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
    img_abs = img_dict[image_name]

    mat_org = cv2.imread(img_abs)
    h, w, c = mat_org.shape
    # mat = cv2.resize(mat_org, (show_w, show_h))
    mat = mat_org
    scale_h = show_h / h
    scale_w = show_w / w
    scale_h = 1
    scale_w = 1
    for idx, target in enumerate(load_dict1['shapes']):
        lname = target['label']
        ff = ''
        if 'head' in lname:
            ff = " ,"
        if lname in show_map:
            lname = show_map[lname]
        else:
            print('label error:',lname)
        if target['shape_type'] == 'rectangle':
            points = np.asarray(target['points'])
            points[:, 0] = points[:, 0] * scale_w
            points[:, 1] = points[:, 1] * scale_h
            points = points.astype(np.int32)
            cv2.rectangle(mat, tuple(points[0]), tuple(points[1]), (255, 0, 0), 2)
            cv2.putText(mat, ff + lname, tuple(points[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            points = np.asarray(target['points'])
            points[:, 0] = points[:, 0] * scale_w
            points[:, 1] = points[:, 1] * scale_h
            p_sets = np.asarray(points, dtype=np.int32)
            p_sets = np.concatenate([p_sets, np.expand_dims(p_sets[0], 0)])
            for i in range(len(p_sets) - 1):
                cv2.line(mat, tuple(p_sets[i]), tuple(p_sets[i + 1]), (0, 0, 255), 2)

            # cv2.polylines(mat, p_sets,True, (222,33,4), 2)
            # cv.putText(img, text, org, fontFace,fontScale,color[, thickness[, lineType[, bottomLeftOrigin]]])
            cv2.putText(mat, lname, tuple(p_sets[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    out_file = os.path.join(img_output,os.path.basename(image_name+'.png'))
    cv2.imwrite(out_file, mat)
    print(out_file)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#
# fw = open(r"D:\Users\Desktop\json_1st\needCheck.txt", 'w')
#
# with open(r"D:\Users\Desktop\json_1st\jsonlist.txt", 'r') as load_f:
#     lines = load_f.readlines()
#     # print(lines)
#     for line in lines:
#         line = line.rstrip()
#         ftt1 = open(json_path1 + line, 'r')
#         load_dict1 = json.load(ftt1)
#         image_name = line.replace("json", "jpg")
#         if not os.path.exists(image_home + image_name):
#             image_name = line.replace("json", "png")
#         if not os.path.exists(image_home + image_name):
#             print(image_name, "file not exist")
#             continue
#
#         mat_org = cv2.imread(image_home + image_name)
#         h, w, c = mat_org.shape
#         mat = cv2.resize(mat_org, (show_w, show_h))
#         scale_h = show_h / h
#         scale_w = show_w / w
#         for idx, target in enumerate(load_dict1['shapes']):
#
#             lname = target['label']
#             ff = ''
#             if 'head' in lname:
#                 ff = " ||"
#             lname = show_map[lname]
#             if target['shape_type'] == 'rectangle':
#                 points = np.asarray(target['points'])
#                 points[:, 0] = points[:, 0] * scale_w
#                 points[:, 1] = points[:, 1] * scale_h
#                 points = points.astype(np.int32)
#                 cv2.rectangle(mat, tuple(points[0]), tuple(points[1]), (222, 33, 44), 1)
#                 cv2.putText(mat, ff + lname, tuple(points[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (222, 33, 44), 2)
#             else:
#                 points = np.asarray(target['points'])
#                 points[:, 0] = points[:, 0] * scale_w
#                 points[:, 1] = points[:, 1] * scale_h
#                 p_sets = np.asarray(points, dtype=np.int32)
#                 p_sets = np.concatenate([p_sets, np.expand_dims(p_sets[0], 0)])
#                 for i in range(len(p_sets) - 1):
#                     cv2.line(mat, tuple(p_sets[i]), tuple(p_sets[i + 1]), (0, 0, 255), 2)
#
#                 # cv2.polylines(mat, p_sets,True, (222,33,4), 2)
#                 cv2.putText(mat, lname, tuple(p_sets[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (222, 33, 44), 2)
#         cv2.imwrite(img_output + image_name, mat)
#         print(img_output + image_name)
#
#
#         # cv2.imshow("aa", mat)
#         # cv2.waitKey(0)
#
#         def on_press(key):
#             # print('{0} pressed'.format(
#             #     key))
#             print(line + '\n')
#             dd = '{0}'.format(key)
#             if dd == "'d'":
#                 print("kill ", line + '\n')
#                 fw.write(line + '\n')
#             return False
#
#         # with Listener(
#         #         on_press=on_press) as listener:
#         #     listener.join()
#
#         # def on_release(key):
#         #     print('{0} release'.format(
#         #         key))
#         #
#         #     if key == "c":
#         #         # Stop listener
#         #         return False
#
#     fw.close()
