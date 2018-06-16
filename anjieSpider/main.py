# -*- coding: utf-8 -*-
'''
    Created by Rechard Catelemmon on 2018/1/19 0019
'''
__author__ = "Rechard Catelemmon"

from  scrapy import cmdline
import os,sys

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    cmdline.execute(["scrapy","crawlall"])