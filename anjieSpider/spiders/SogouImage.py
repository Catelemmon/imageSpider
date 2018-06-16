# -*- coding: utf-8 -*-
import re
import urllib

import scrapy
from pypinyin import pinyin
from scrapy import Request
from scrapy.loader import ItemLoader

from ..items import SougouImageItem
from ..utils.read_items import *

class SogouimageSpider(scrapy.Spider):
    name = 'SogouImage'
    allowed_domains = ['pic.sogou.com']
    url_template='http://pic.sogou.com/pics?query={word}&mode=1&start={pageNum}&reqType=ajax&reqFrom=resul'
    items_type=None
    custom_settings = {
        "ITEM_PIPELINES":{
        'anjieSpider.pipelines.BaiduImageFilePipeline': 1,
        'anjieSpider.pipelines.ImageClassification': 2,
        }
    }

    def start_requests(self):
        spider_json_obj=read_spider_item()
        self.items_type = spider_json_obj["targets_type"]  # 读取待爬取条目的类型
        input_items_need_get = spider_json_obj["targets"]  # 待爬取的条目对象的数组
        for input_dict_item in input_items_need_get:
            yield Request(self.url_template.format(word=input_dict_item["target_name"],pageNum=0))
            for i in range(48,input_dict_item["page_num"]*48,48):
                yield Request(self.url_template.format(word=input_dict_item["target_name"],pageNum=i))

    def parse(self, response):
        res=response.body.decode(response.encoding).strip()
        json_obj=json.loads(res)
        items_list=json_obj["items"]
        item=SougouImageItem()
        for i in items_list:
            img_thumb_url=i.get("thumbUrl","")
            item['img_thumb_url']=img_thumb_url
            img_hd_url=i.get("pic_url","")
            if img_hd_url!="":
                item["img_hd_url"]=img_hd_url
            img_entry_title=i.get("title","")
            item["img_entry_title"]=img_entry_title
            img_entry=urllib.parse.unquote(re.search("query=(.*?)&",response.url).group(1))
            item["img_entry"]=img_entry
            item["img_entry_first_letter"]=pinyin(img_entry)[0][0][0].upper()
            item["img_entry_type"]=self.items_type
            item["img_entry_source"]=self.name
            yield item
