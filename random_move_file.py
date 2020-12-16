#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'ImgProcess'
__author__ = 'deagle'
__date__ = '12/14/2020 16:40'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
##深度学习过程中，需要制作训练集和验证集、测试集。

import os, random, shutil


def moveFile(fileDir, tarDir, picknumber=1):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    # filenumber = len(pathDir)
    # rate = 0.1  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    # picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    # print(sample)
    for name in sample:
        shutil.move(fileDir + name, tarDir + name)
    return


def moveFile(fileDir, tarDir, rate=0.1):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.1  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    # print(sample)
    for name in sample:
        shutil.move(fileDir + name, tarDir + name)
    return

def travel(folder):
    target_file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            f = os.path.join(root, file)
            target_file_list.append(f)
    return target_file_list

'''
分成n份
最后一份会多，多出来的是余数个数
'''
def moveFile(fileDir, tarDir, devide=2):
    pathDir = travel(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    print('devide to:',devide)
    picknumber = int(filenumber / devide)
    print('num per:',picknumber)
    for i in range(1, devide):
        print(i,'st')
        pathDirTmp = travel(fileDir)
        sample = random.sample(pathDirTmp, picknumber)  # 随机选取picknumber数量的样本图片
        if not os.path.exists(tarDir + str(i)):
            os.makedirs(tarDir + str(i))
        for f in sample:
            name = os.path.basename(f)
            shutil.move(f, tarDir + str(i) + '/' + name)
    # move 剩下的
    pathDir2List = travel(fileDir)
    if not os.path.exists(tarDir + str(i+1)):
        os.makedirs(tarDir + str(i+1))
    for f in pathDir2List:
        name = os.path.basename(f)
        shutil.move(f, tarDir + str(i+1) + '/' + name)
    return


if __name__ == '__main__':
    fileDir = r"E:\非机动车数据\筛选后数据集\处理后\待分发\\"  # 源图片文件夹路径
    tarDir = r"E:\非机动车数据\筛选后数据集\处理后\new\\"  # 源图片文件夹路径
    if not os.path.exists(tarDir):
        os.makedirs(tarDir)
    moveFile(fileDir, tarDir, devide=9)
