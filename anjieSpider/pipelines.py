# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import functools

import os

import re

import shutil
import threading

from scrapy import Request
from urllib.parse import to_bytes

from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings
from .settings import FILES_STORE


class BaiduImageFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return Request(url=item["img_hd_url"],meta={"item":item})

    def file_path(self, request, response=None, info=None):
        file_guid=hashlib.sha1(request.url.encode("utf8")).hexdigest()
        file_ext=re.search("\.\w+$",request.url).group(0)
        return "tmp/%s%s"%(file_guid,file_ext)

    def item_completed(self, results, item, info):
        # thumb_res,hd_res=results[0],results[1]
        # thumb_has_downloaded,thumb_res_info=thumb_res
        # if thumb_has_downloaded:
        #     item["img_thumb_path"]=os.path.join(self.store.basedir,thumb_res_info["path"].replace("/","\\"))
        hd_has_downloaded,hd_res_info=results[0][0],results[0][1]
        if hd_has_downloaded:
            item["img_hd_path"]=os.path.join(self.store.basedir,hd_res_info["path"].replace("/","\\"))
        else:
            item["img_hd_path"]=""
        return item

class ImageClassification(object):

    abs_root_dir=get_project_settings().get("FILES_STORE")

    def process_item(self,item,spider):
        # thumb_dst_path = os.path.join(self.abs_root_dir,item["img_entry_type"],
        #                                     item["img_entry_first_letter"],item["img_entry"],
        #                                                   item["img_entry_source"],"thumb")
        # self.move_img(item["img_thumb_path"],thumb_dst_path )
        # img_thumb_name=os.path.split(item["img_thumb_path"])[1]
        # item["img_thumb_path"]=os.path.join(thumb_dst_path,img_thumb_name)
        # item["img_thumb_name"]=img_thumb_name

        if item["img_hd_path"]!="":
            hd_dst_path=os.path.join(self.abs_root_dir, item["img_entry_type"],
                                                               item["img_entry_first_letter"], item["img_entry"],
                                                               item["img_entry_source"],)
            self.move_img(item["img_hd_path"],hd_dst_path)
            img_hd_name=os.path.split(item["img_hd_path"])[1]
            item["img_hd_path"]=os.path.join(hd_dst_path,img_hd_name)
            item["img_hd_name"]=img_hd_name
        else:
            item["img_hd_name"] =""
        return item


    def move_img(self,src_file, dst_path):
        try:
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
            shutil.move(src_file, dst_path)
        except:
            pass

class BingImagePipeline(object):

    def process_item(self,item,spider):
        item["img_hd_name"] = hashlib.sha1(item["img_hd_url"].encode("utf8")).hexdigest() + "." + item["img_type"]
        file = self.check_path()+"\\"+item["img_hd_name"]
        with open(file,"wb") as img:
            img.write(item["img_content"])
        item["img_content"] = None
        item["img_hd_path"]=file.replace("\\","/")
        return item

    def check_path(self):
        path=os.path.join(FILES_STORE,"tmp")
        if not os.path.exists(path):
            os.mkdir(path)
        return path

class MongoDBPipeline(object): # 数据库待写入
    pass