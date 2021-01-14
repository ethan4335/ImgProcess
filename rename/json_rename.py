#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/14/2020 11:32'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
# import my_common.Files
import os
import json

'''
00004_22250
zmj_20201211_v00007_itv160_2
'''


def main():
    path = r'D:\work_source\CV_Project\datasets\labels_original\7'

    # target_file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if '.json' in file:

                # tmp_dict = []
                with open(os.path.join(root, file),encoding='utf-8') as f:
                    data = json.load(f)
                    data['imagePath'] = 'rename_7_'+file
                    tmp_dict = data
                f.close()

                with open(os.path.join(root, file),encoding='utf-8',mode='w') as r:
                    json.dump(tmp_dict, r)
                r.close()

                os.rename(os.path.join(root, file), os.path.join(root, 'rename_7_' + file))





if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
