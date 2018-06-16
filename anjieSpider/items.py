# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjiespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BaiduImageItem(scrapy.Item):
    img_thumb_url=scrapy.Field() # 图片的缩略图的链接
    img_hd_url=scrapy.Field() # 图片的高清图的链接
    img_thumb_url_id=scrapy.Field() # 图片的缩略图url的md5加密id(方便扩展到关系型数据库,以这个id作为主键)
    img_thumb_path=scrapy.Field() # 图片的缩略图的存储路径
    img_hd_path=scrapy.Field() # 高清图的存储路径
    img_FromPageTitle=scrapy.Field() # 图片来源网页的标题
    img_entry=scrapy.Field() # 当前爬取的词条
    img_entry_first_letter=scrapy.Field() # 爬取词条的第一个字母
    img_entry_type=scrapy.Field() # 爬取的词条的类型
    img_entry_source=scrapy.Field() # 爬取词条的来源
    img_thumb_name=scrapy.Field() # 图片的标清文件名字
    img_hd_name=scrapy.Field() # 图片的高清图文件的名字

class SougouImageItem(scrapy.Item):
    img_thumb_url=scrapy.Field() # 图片的缩略图链接
    img_thumb_path=scrapy.Field() # 缩略图保存的路径
    img_hd_url=scrapy.Field() # 图片的高清图的链接
    img_hd_path=scrapy.Field() # 高清图片保存的路径
    img_entry_title=scrapy.Field() # 图片的标题
    img_thumb_url_id=scrapy.Field() #图片的缩略图的id
    img_entry=scrapy.Field() # 爬取的词条的名称
    img_entry_first_letter=scrapy.Field() # 图片词条的第一个字母
    img_entry_type=scrapy.Field() # 词条的类型(人物 军舰等)
    img_entry_source=scrapy.Field()  # 图片的词条的来源(sogou baidu bing etc.)
    img_hd_name=scrapy.Field() # 高清图片的名字
    img_thumb_name=scrapy.Field() # 缩略图的名字

class BingImageItem(scrapy.Item):
    img_hd_url=scrapy.Field() # 图片的高清图链接
    img_hd_path=scrapy.Field() # 图片的高清图路径
    img_entry = scrapy.Field() # 搜索的词条的名称
    img_entry_first_letter=scrapy.Field() #词条的首字母
    img_entry_type=scrapy.Field() # 词条的类型
    img_entry_source=scrapy.Field() # 词条的来源
    img_hd_name=scrapy.Field() # 高清图的名字
    img_content=scrapy.Field() # 图片的二进制内容
    img_type =scrapy.Field() # 图片的类型
