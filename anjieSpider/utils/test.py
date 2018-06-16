# -*- coding: utf-8 -*-
'''
    Created by Rechard Catelemmon on 2018/3/30 0030
'''
import re

import requests

__author__ = "Rechard Catelemmon"


if __name__ == '__main__':
    resp=requests.get('https://cn.bing.com/images/async?q=迪丽热巴&first=0&count=35&relo=6&relp=6&lostate=c&mmasync=1')
    pattern = re.compile('<img.+?src="(https://.+?cn.bing.net.+?);.+?alt="迪丽热巴.+?>?')
    res=resp.content.decode(resp.encoding)
    url_list=pattern.findall(res)
    print(url_list)
    pass