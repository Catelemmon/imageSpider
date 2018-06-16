# -*- coding: utf-8 -*-
'''
    Created by Rechard Catelemmon on 2018/3/22 0022
'''
__author__ = "Rechard Catelemmon"

import json
from ..settings import *


def read_spider_item():
    items_json_file = open(SPIDER_ITEM_PATH, "r", encoding="utf-8")  # 读取待爬取的条目的文件
    items_json = json.load(items_json_file)  # 加载json文件为python对象
    items_json_file.close()
    return items_json