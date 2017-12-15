# -*- coding: utf-8 -*-

# Scrapy settings for quotetutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'quotetutorial'

SPIDER_MODULES = ['quotetutorial.spiders']
NEWSPIDER_MODULE = 'quotetutorial.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'quotetutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/57.0',
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    'Cookie': 'q_c1=54083c448891421ebbf5a5f56236a8dc|1511964196000|1511964196000; _zap=1c685b2c-e226-4505-ac09-545f9a871d21; aliyungf_tc=AQAAAMN5fRz1XQYAt5JEeWObfILrES/9; l_n_c=1; _xsrf=92a54de8eed96aaadb49f13e5f04aa09; r_cap_id="MjUyZTczYzAxZjEwNDM4ZGJlYzM5MzkxZDE1OWI5YjM=|1512836641|50caa099d985fa9fd555a10b555f7a27ba2c01e0"; cap_id="Y2RiYTU2MDg3NTIzNGRjY2I5ZTQxZTg2MzM4YjA0YmE=|1512836641|c6c91b91ff8e446f87c76b6e23318f1f2493f2dd"; l_cap_id="MmUxYjNjMTZjYzM5NDFiZWFlZDRkNTI3YTNkZWEwZDA=|1512836641|2a83671b52ac7703aec3012829a3bfb0771885e6"; d_c0="AJBCif38zgyPTtMZsXRXks40mdT3m2C_IoQ=|1512829176"; __utma=51854390.776446348.1512829177.1512832538.1512836644.3; __utmc=51854390; __utmz=51854390.1512832538.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=51854390.000--|3=entry_date=20171129=1; _xsrf=92a54de8eed96aaadb49f13e5f04aa09; __utmb=51854390.0.10.1512836644; capsion_ticket="2|1:0|10:1512836665|14:capsion_ticket|44:MjM2MmM1ZmMzYzgyNDM0YWFmMzU0NDI0NmZiYzE5Mzc=|8a95171f6be93ac10d804f360da29320141c95ba6621b11aeceb850faa9c20a0"; z_c0="2|1:0|10:1512836695|4:z_c0|92:Mi4xbkhkV0JRQUFBQUFBa0VLSl9mek9EQ1lBQUFCZ0FsVk5WMXdaV3dBb3U0QzRjamFFYzFiRmpqWjBrQ1ltQTh5akFB|64a639e040330e41649db912aa16f84c3a18ce8a67824f2ff94cebb4b85d9ac2"; unlock_ticket="AJACsNEk_gsmAAAAYAJVTV8VLFoJteOemzpQn33JzmX1FK05OB6AaA=="'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'quotetutorial.middlewares.QuotetutorialSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'quotetutorial.middlewares.MyCustomDownloaderMiddleware': 543,
#    'quotetutorial.middlewares.ProxyMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'quotetutorial.pipelines.TextPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
