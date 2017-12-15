# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if spider.name == 'quotes':
            if item['text']:
                if len(item['text']) > self.limit:
                    item['text'] = item['text'][0:self.limit].rstrip() + '...'
                    return item
            else:
                DropItem('Miss Text')

