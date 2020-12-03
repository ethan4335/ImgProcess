"""author: 文龙"""

import numpy as np
import json
import os
# import shutil
import cv2
# import keyboard
# import tty
# import termios
# import sys
# from pynput.keyboard import Key, Listener

# from pynput.keyboard import Key, Listener

from pynput.keyboard import Listener

#
# def readchar():
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch
#
#
# def readkey(getchar_fn=None):
#     getchar = getchar_fn or readchar
#     c1 = getchar()
#     if ord(c1) != 0x1b:
#         return c1
#     c2 = getchar()
#     if ord(c2) != 0x5b:
#         return c1
#     c3 = getchar()
#     return chr(0x10 + ord(c3) - 65)

#
# label_name = {'160001': '二轮电动车（无遮阳棚）',
#               '160009': '戴头盔的人头部',
#               '16000C': '车牌不规范',
#               '160008': '斑马线',
#               '16000D': '混合区域',
#               '160006': '停止线',
#               '160007': '车道线',
#               '16000E': '未定义',  # 未定义是摩托车?
#               '16000B': '车牌',
#               '16000A': '不戴头盔的人头部',
#               '160003': '三轮电动车',
#               '160002': '二轮电动车（有遮阳棚）',
#               '160004': '机动车',
#               '160005': '车道虚线'
#               }
#
# label_map1 = {'160001': 0,  # '二轮电动车（无遮阳棚）'
#               '160003': 1,  # '三轮电动车'
#               '160002': 2,  # '二轮电动车（有遮阳棚）'
#
#               '160004': 3,  # '机动车'
#               '16000E': 4,  # '未定义' # 未定义是摩托车?
#               '16000D': 11,  # '混合区域' # blank?
#               }
# show_label = {
#     '160001': 'ebike2_1',  # '二轮电动车（无遮阳棚）'
#     '160003': "ebike3",  # '三轮电动车'
#     '160002': "ebike2_2",  # '二轮电动车（有遮阳棚）'
#
#     '160004': "vehicle",  # '机动车'
#     '16000E': "motobike",  # '未定义' # 未定义是摩托车?
#     '16000D': "blank",  # '混合区域' # blank?
#     '160009': "head_1",  # '戴头盔的人头部'
#     '16000A': "head_2",  # '不戴头盔的人头部'
#     '16000B': "chepai",  # '车牌'
#     '16000C': "shangbiao",  # '车牌不规范'
# }
#
# label_map2 = {
#     '160009': 0,  # '戴头盔的人头部'
#     '16000A': 1,  # '不戴头盔的人头部'
#     '16000B': 2,  # '车牌'
#     '16000C': 3,  # '车牌不规范'
# }

dict_new_label = {
'ebike3_back':'rectangle',
'ebike2_other':'rectangle',
'head_with_helmet':'rectangle',
'license_moto':'rectangle',
'blank':'polygon',
'ebike2_back':'rectangle',
'head_without_helmet':'rectangle',
'license_ebike':'rectangle',
'license_other':'rectangle',
'ebike3_other':'rectangle',
'ebike2_front':'rectangle',
'ebike2_sunshade_other':'rectangle',
}

json_path1 = r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\label/"

image_home = r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\img/"
total = 0

show_h = np.int32(720*1.3)
show_w = np.int32(1280*1.3)
# recheck list
fw = open(r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample/need_check.txt", 'w')

with open(r"D:\work_source\CV_Project\datasets\biaozhu_20201203\sample\label_list.txt", 'r') as load_f:
    lines = load_f.readlines()
    # print(lines)
    for line in lines:
        print('read label json: %s'%(json_path1+line))
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
        scale_h = show_h/h
        scale_w = show_w/w
        for idx, target in enumerate(load_dict1['shapes']):
            # di[target['f_code']] = target['f_name']

            if target['label'] in dict_new_label.keys():
                # lname = show_label[target['f_code']]
                ff = ''
                # if 'head' in lname:
                #     ff = "        "
                if target['shape_type'] == 'rectangle':
                    points = target['points']
                    print(points[0][0])

                    x = np.int(points[0][0]*scale_w)
                    y = np.int(points[0][1]*scale_h)
                    w = np.int((points[1][0] - points[0][0])*scale_w)
                    h = np.int((points[1][1] - points[0][1])*scale_h)
                    cv2.rectangle(mat, (x, y), (x + w, y + h), (222, 33, 44), 1)
                    cv2.putText(mat, ff, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (222, 33, 44), 2)
                elif target['shape_type'] == 'rectangle':
                    points = target['points']
                    p_sets = []
                    for p in points:
                        p_sets.append([p[0]*scale_w, p[1]*scale_h])
                    p_sets = np.asarray(p_sets, dtype=np.int32)

                    for i in range(len(p_sets) - 1):
                        cv2.line(mat, tuple(p_sets[i]), tuple(p_sets[i + 1]), (0, 0, 255), 2)

                    # cv2.polylines(mat, p_sets,True, (222,33,4), 2)
                    cv2.putText(mat, tuple(p_sets[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (222, 33, 44),
                                2)
            else:
                continue
        cv2.imshow("aa", mat)
        cv2.waitKey(0)


        def on_press(key):
            # print('{0} pressed'.format(
            #     key))
            print(line + '\n')
            dd = '{0}'.format(key)
            if dd == "'d'":
                print("kill ", line + '\n')
                fw.write(line + '\n')
            return False


        with Listener(
                on_press=on_press) as listener:
            listener.join()
        # def on_release(key):
        #     print('{0} release'.format(
        #         key))
        #
        #     if key == "c":
        #         # Stop listener
        #         return False

    fw.close()
