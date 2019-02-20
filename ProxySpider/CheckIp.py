# -*- coding: utf-8 -*-

import requests
from pymongo import MongoClient


def check():
    clent = MongoClient("localhost", 27017)
    db = clent['Anjuke']
    proxyTable = db['proxys']
    collection = proxyTable.find()
    for each in collection:
        proxy = str(each['host']) + ":" + str(each['port'])
        proxies = {"http": "http://" + proxy, "https": "http://" + proxy, }
        try:
            requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
        except:
            print u"-----%s------代理无效--------------" % proxy
            proxyTable.delete_one(each)


while True:
    check()
