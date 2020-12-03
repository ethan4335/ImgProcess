import numpy as np
import json
import os
import shutil
import cv2
import keyboard
# import tty
# import termios
import sys
from pynput.keyboard import Key, Listener

total_map = {'ebike3_back': 0,
             'ebike2_other': 0,
             'head_with_helmet': 0,
             'license_moto': 0,
             'blank': 0,
             'ebike2_back': 0,
             'head_without_helmet': 0,
             'license_ebike': 0,
             'license_other': 0,
             'ebike3_other': 0,
             'ebike2_front': 0,
             'ebike2_sunshade_other': 0}
show_map = {'ebike3_back': 'e3b',
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

json_path1 = r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\label/"

image_home = r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\img/"
img_output = r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\img_abeled/"
total = 0

show_h = np.int32(720 * 1.3)
show_w = np.int32(1280 * 1.3)

fw = open(r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample/need_check.txt", 'w')

with open(r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\label_list.txt", 'r') as load_f:
    lines = load_f.readlines()
    # print(lines)
    for line in lines:
        line = line.rstrip()
        ftt1 = open(json_path1 + line, 'r')
        load_dict1 = json.load(ftt1)
        image_name = line.replace("json", "jpg")
        if not os.path.exists(image_home + image_name):
            image_name = line.replace("json", "png")
        if not os.path.exists(image_home + image_name):
            print(image_name, "file not exist")
            continue

        mat_org = cv2.imread(image_home + image_name)
        h, w, c = mat_org.shape
        mat = cv2.resize(mat_org, (show_w, show_h))
        scale_h = show_h / h
        scale_w = show_w / w
        for idx, target in enumerate(load_dict1['shapes']):

            lname = target['label']
            ff = ''
            if 'head' in lname:
                ff = " ||"
            lname = show_map[lname]
            if target['shape_type'] == 'rectangle':
                points = np.asarray(target['points'])
                points[:, 0] = points[:, 0] * scale_w
                points[:, 1] = points[:, 1] * scale_h
                points = points.astype(np.int32)
                cv2.rectangle(mat, tuple(points[0]), tuple(points[1]), (222, 33, 44), 1)
                cv2.putText(mat, ff + lname, tuple(points[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (222, 33, 44), 2)
            else:
                points = np.asarray(target['points'])
                points[:, 0] = points[:, 0] * scale_w
                points[:, 1] = points[:, 1] * scale_h
                p_sets = np.asarray(points, dtype=np.int32)
                p_sets = np.concatenate([p_sets, np.expand_dims(p_sets[0], 0)])
                for i in range(len(p_sets) - 1):
                    cv2.line(mat, tuple(p_sets[i]), tuple(p_sets[i + 1]), (0, 0, 255), 2)

                # cv2.polylines(mat, p_sets,True, (222,33,4), 2)
                cv2.putText(mat, lname, tuple(p_sets[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (222, 33, 44), 2)
        cv2.imwrite(img_output + image_name,mat)
        print(img_output + image_name)


        # cv2.imshow("aa", mat)
        # cv2.waitKey(0)

        def on_press(key):
            # print('{0} pressed'.format(
            #     key))
            print(line + '\n')
            dd = '{0}'.format(key)
            if dd == "'d'":
                print("kill ", line + '\n')
                fw.write(line + '\n')
            return False


        # with Listener(
        #         on_press=on_press) as listener:
        #     listener.join()

        # def on_release(key):
        #     print('{0} release'.format(
        #         key))
        #
        #     if key == "c":
        #         # Stop listener
        #         return False

    fw.close()
