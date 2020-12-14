#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/11/2020 10:57'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import numpy as np
import imageio
import rawpy
import sys
import os
import imageio
import matplotlib.pylab as plt


input_folder = r'D:\Users\Desktop\pics'
output_folder = r'D:\Users\Desktop\output'


def convert(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            f = os.path.join(root, file)

            print("Converting file: " + f)
            if not os.path.isfile(f):
                print("The file doesn't exist!")
                sys.exit()

            raw = rawpy.imread(f)

            # 直接调用postprocess可能出现偏色问题
            # rgb = raw.postprocess()

            # 以下两行可能解决偏色问题，output_bps=16表示输出是 16 bit (2^16=65536)需要转换一次
            im = raw.postprocess(use_camera_wb=True, half_size=True, no_auto_bright=True, output_bps=16)
            rgb = np.float32(im / 65535.0*255.0)
            rgb = np.asarray(rgb,np.uint8)

            imageio.imsave(os.path.join(output_folder,f.replace('ARW','png')), rgb)


def extract_bayer_channels(raw):
    ch_B = raw[1::2, 1::2]
    ch_Gb = raw[0::2, 1::2]
    ch_R = raw[0::2, 0::2]
    ch_Gr = raw[1::2, 0::2]

    return ch_R, ch_Gr, ch_B, ch_Gb


if __name__ == "__main__":
    convert(output_folder)
