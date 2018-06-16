# -*- coding: utf-8 -*-
'''
    Created by Rechard Catelemmon on 2018/3/31 0031
'''
__author__ = "Rechard Catelemmon"

from setuptools import setup, find_packages

setup(name='scrapy-mymodule',
    entry_points={
        'scrapy.commands': ['crawlall=anjieSpider.commands:crawlall',],
    },
)