
import os
import cv2
import numpy as np
import json





def add_blank_area(imgs_dir, json_dir, out_img_dir):
    img_dict = {}
    json_dict = {}
    for root, dirs, files in os.walk(imgs_dir):
        for file in files:
            f = os.path.join(root, file)
            img_name = os.path.splitext(file)[0]
            img_dict[img_name] = f

    for root, dirs, files in os.walk(json_dir):
        for file in files:
            f = os.path.join(root, file)
            j_name = os.path.splitext(file)[0]
            if 'invalied' in f or 'json' not in f:
                continue
            json_dict[j_name] = f

    for name in img_dict.keys():
        if name not in json_dict.keys():
            print('json error:', name)
            continue
        with open(json_dict[name]) as f:
            json_content = json.load(f)
            img = cv2.imread(img_dict[name])
            shapes = json_content['shapes']
            for each_shape in shapes:
                # rectangle
                # if each_shape['label'] in select_labels:
                #     cv2.rectangle(img, (int(each_shape['points'][0][0]), int(each_shape['points'][0][1])),
                #                   (int(each_shape['points'][1][0]), int(each_shape['points'][1][1])),
                #                   (0, 255, 0), 2)
                #     cv2.putText(img, each_shape['label'],
                #                 (int(each_shape['points'][0][0]), (int(each_shape['points'][0][1]))),
                #                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                # polygon
                if each_shape['label'] == 'blank':
                    obj_points = np.array([[0, 0]], np.int32)
                    for point in each_shape['points']:
                        obj_points = np.concatenate((obj_points, np.array([[point[0], point[1]]], np.int32)), axis=0)
                    obj_points = np.delete(obj_points, [0], axis=0)
                    # def fillPoly(img, pts, color, lineType=None, shift=None, offset=None)
                    img = cv2.fillConvexPoly(img, obj_points, (0, 0, 0), 8, 0)
                    print(os.path.join(out_img_dir, os.path.basename(img_dict[name])))
                    cv2.imwrite(os.path.join(out_img_dir, os.path.basename(img_dict[name])), img)

img_home = r'D:\work_source\test_env_py\add_blank_area\img_need_blank'
json_home = r'D:\work_source\test_env_py\add_blank_area\json_contain_blank'
img_out = r'D:\work_source\test_env_py\add_blank_area\img_blank_1'

if not os.path.exists(img_out):
    os.mkdir(img_out)

add_blank_area(img_home,json_home,img_out)