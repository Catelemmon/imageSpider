# -*- coding: utf-8 -*-
import re
import urllib

import scrapy
from pypinyin import pinyin
from scrapy import Request
from scrapy.loader import ItemLoader

from ..items import BingImageItem
from ..utils.read_items import read_spider_item


class BingspiderSpider(scrapy.Spider):
    name = 'BingSpider'
    allowed_domains = ['cn.bing.com/images']
    url_templates="https://cn.bing.com/images/async?q={word}&first={start_image_num}&count=35&relo=6&relp=6&lostate=c&mmasync=1"
    items_type=None
    custom_settings = {
        "ITEM_PIPELINES":{
            "anjieSpider.pipelines.BingImagePipeline":1,
            'anjieSpider.pipelines.ImageClassification': 2,
        }
    }

    def start_requests(self):
        spider_json_obj=read_spider_item()
        self.items_type = spider_json_obj["targets_type"]
        input_items_need_get = spider_json_obj["targets"]
        for input_dict_item in input_items_need_get:
            yield Request(self.url_templates.format(word=input_dict_item['target_name'],start_image_num=0))
            for i in range(37,input_dict_item['page_num']*37,37):
                yield Request(self.url_templates.format(word=input_dict_item['target_name'],start_image_num=i))

    def parse(self, response):
        # res=response.body.decode(response.encoding)
        res=response.text
        img_entry=urllib.parse.unquote(re.search("q=(.*?)&", response.url).group(1))
        pattern=re.compile('<img.+?src="(https://.+?cn.bing.net.+?);.+?alt=".+?{word}.+?>?'.format(word=img_entry))
        img_url_list=pattern.findall(res)
        img_entry_first_letter=pinyin(img_entry)[0][0][0].upper()
        for url in img_url_list:
            yield Request(url=url,meta={"img_entry":img_entry,"img_entry_first_letter":img_entry_first_letter},callback=self.parse_detail,dont_filter=True)

    def parse_detail(self,response):
        item=BingImageItem()
        item["img_entry_type"]=self.items_type
        item["img_entry_source"]=self.name
        item["img_entry"]=response.meta["img_entry"]
        item["img_hd_url"]=response.url
        img_type=response.headers[b'Content-Type'].decode(response.headers.encoding).split('/')[1]
        item["img_type"]=img_type
        item["img_content"]=response.body
        item["img_entry_first_letter"]=response.meta["img_entry_first_letter"]
        yield item
