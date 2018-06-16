# -*- coding: utf-8 -*-

# Scrapy settings for anjieSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'anjieSpider'

SPIDER_MODULES = ['anjieSpider.spiders']
NEWSPIDER_MODULE = 'anjieSpider.spiders'

PROJECT_DIR=os.path.abspath(os.path.dirname(__file__))
SPIDER_ITEM_PATH=PROJECT_DIR+"\\spiders\\spider_items.json"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
MEDIA_ALLOW_REDIRECTS = True
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept':'application/json, text/javascript, */*; q=0.01',
#    "Accept-Encoding":"gzip, deflate, br",
#    "Accept-Language":"zh-CN,zh;q=0.9",
#    "Cookie":"BAIDUID=F153E1FE9E42C58EA2747FBDDB631EF1:FG=1; BIDUPSID=F153E1FE9E42C58EA2747FBDDB631EF1; PSTM=1516443687; PSINO=3; BDRCVFR[i-rd_-eQEYn]=mk3SLVN4HKm; H_PS_PSSID=; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null",
#     "Host":"image.baidu.com",
#     "X-Requested-With":"XMLHttpRequest"
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'anjieSpider.middlewares.AnjiespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'anjieSpider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'anjieSpider.pipelines.BaiduImageFilePipeline':1,
   'anjieSpider.pipelines.ImageClassification':2,
}
COMMANDS_MODULE = 'anjieSpider.commands'

FILES_STORE = PROJECT_DIR+"\\image_files"
IMAGES_URLS_FIELD="img_url_tuple"
front_img_url="img_url_tuple"

DOWNLOAD_DELAY = 10

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


