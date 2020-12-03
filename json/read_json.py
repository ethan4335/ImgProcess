#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pic_note'
__author__ = 'deagle'
__date__ = '7/21/2020 9:52'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓     ┏┓
            ┏━┛┻━━━━━┛┻━┓
            ┃     ☃     ┃
            ┃  ┳┛   ┗┳  ┃
            ┃     ┻     ┃
            ┗━┓       ┏━┛
              ┃       ┗━━━━┓
              ┃   神兽保佑  ┣┓
              ┃   永无BUG！ ┣┛
              ┗━┓┓┏━━━━┳┓┏━┛
                ┃┫┫    ┃┫┫
                ┗┻┛    ┗┻┛
"""

import json

#注意：不带s的用于操作文件，带s的用于数据类型的转换。

import json,time
# save data to json file
def store(data):
    with open('data.json', 'w') as fw:
        # 将字典转化为字符串
        # json_str = json.dumps(data)
        # fw.write(json_str)
        # 上面两句等同于下面这句
        json.dump(data,fw)
# load json data from file
def load():
    with open('data.json','r') as f:
        data = json.load(f)
        return data


if __name__ == "__main__":
    json_data = '{"login":[{"username":"aa","password":"001"},{"username":"bb","password":"002"}],"register":[{"username":"cc","password":"003"},{"username":"dd","password":"004"}]}'
    # 函数是将json格式数据转换为字典
    data = json.loads(json_data)
    store(data)

    data = load()
    print(data)
