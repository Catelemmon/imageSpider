# -*- coding: utf-8 -*-
import codecs
import json

import re
import urllib

import scrapy
from pypinyin import pinyin
from scrapy import Request

from ..items import BaiduImageItem
from ..settings import *
from ..utils.read_items import *

class BaiduimageSpider(scrapy.Spider):
    name = 'baiduimage'
    allowed_domains = ['image.baidu.com']
    url_template = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pageNum}&rn=30"
    items_type=None
    custom_settings = {
        "ITEM_PIPELINES":{
        'anjieSpider.pipelines.BaiduImageFilePipeline': 1,
        'anjieSpider.pipelines.ImageClassification': 2,
        }
    }

    def start_requests(self): # 重写start_requests 方法
        spider_json_obj=read_spider_item()
        self.items_type=spider_json_obj["targets_type"] # 读取待爬取条目的类型
        input_items_need_get=spider_json_obj["targets"] # 待爬取的条目对象的数组
        for input_dict_item in input_items_need_get:
            yield Request(self.url_template.format(word=input_dict_item["target_name"], pageNum=-1))
            # 百度图片的第一页的条目爬取
            for i in range(30,input_dict_item["page_num"]*30,30):
                yield Request(self.url_template.format(word=input_dict_item["target_name"], pageNum=i))
                # 百度图片的翻页的实现


    def decrypt_hd_img_addr(self, url): # 高清图片解密函数
        symbol_table = { # 解密符号表
            '_z2C$q': ':',
            '_z&e3B': '.',
            'AzdH3F': '/'
        }
        char_table = { # 解密字符表
            'w': 'a',
            'k': 'b',
            'v': 'c',
            '1': 'd',
            'j': 'e',
            'u': 'f',
            '2': 'g',
            'i': 'h',
            't': 'i',
            '3': 'j',
            'h': 'k',
            's': 'l',
            '4': 'm',
            'g': 'n',
            '5': 'o',
            'r': 'p',
            'q': 'q',
            '6': 'r',
            'f': 's',
            'p': 't',
            '7': 'u',
            'e': 'v',
            'o': 'w',
            '8': '1',
            'd': '2',
            'n': '3',
            '9': '4',
            'c': '5',
            'm': '6',
            '0': '7',
            'b': '8',
            'l': '9',
            'a': '0',
        }
        # str 的translate方法需要用单个字符的十进制unicode编码作为key
        # value 中的数字会被当成十进制unicode编码转换成字符
        # 也可以直接用字符串作为value
        char_table = {ord(key): ord(value) for key, value in char_table.items()}
        # 先替换字符串
        for key, value in symbol_table.items():
            url = url.replace(key, value)
        # 再替换剩下的字符
        return url.translate(char_table)

    def parse(self, response):
        img_item= BaiduImageItem()
        str_json = response.body.decode("utf-8") # 对返回的json数据进行解码
        img_jsonobj_elems=json.loads(str_json)["data"] # 把json数据加载为python对象
        for img_jsonobj_elem in img_jsonobj_elems:
            img_thumb_url = img_jsonobj_elem.get("thumbURL","") # 处理图片的thumUrl
            img_middle_url=img_jsonobj_elem.get("middleURL","")
            img_hd_url=self.decrypt_hd_img_addr(img_jsonobj_elem.get("objURL",""))
            if img_thumb_url=="":
                if img_middle_url!="":
                    img_thumb_url=img_middle_url
                elif img_hd_url!="":
                    img_thumb_url=img_hd_url
                else:
                    continue
            if img_hd_url=="":
                img_hd_url=img_thumb_url
            img_item["img_thumb_url"]=img_thumb_url
            img_item["img_hd_url"]=img_hd_url
            img_item["img_FromPageTitle"]=img_jsonobj_elem.get("fromPageTitle","")
            img_entry=urllib.parse.unquote(re.search("word=(.*?)&",response.url).group(1))
            img_item["img_entry"]=img_entry
            img_item["img_entry_first_letter"]=pinyin(img_entry)[0][0][0].upper()
            img_item["img_entry_type"]=self.items_type
            img_item["img_entry_source"]=self.name
            yield img_item