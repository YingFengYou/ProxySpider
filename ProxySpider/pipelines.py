# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import telnetlib
import requests


class ProxyspiderPipeline(object):

    def __init__(self):
        self.clinet = pymongo.MongoClient("localhost", 27017)
        self.db = self.clinet["Anjuke"]
        self.proxyItem = self.db["ProxyAll"]

    def process_item(self, item, spider):
        proxy = item['host'] + ":" + item['port']
        proxies = {"http": "http://" + proxy, "https": "http://" + proxy, }
        try:
            requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
            self.proxyItem.insert(dict(item))
        except:
            print u"-----%s------代理无效--------------" % proxy
