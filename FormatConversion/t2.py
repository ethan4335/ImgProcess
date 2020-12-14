from __future__ import division
import os, scipy.io
import numpy as np
import rawpy
import glob


import rawpy
import imageio
import matplotlib.pylab as plt

raw = rawpy.imread(r'D:\Users\Desktop\pics\DSC06746.ARW')

#直接调用postprocess可能出现偏色问题
rgb = raw.postprocess()

imageio.imsave(r'D:\Users\Desktop\pics\image.jpg', rgb)
