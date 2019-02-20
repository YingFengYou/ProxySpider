# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from ProxySpider.items import ProxyspiderItem


class ProxyspiderSpider(scrapy.Spider):
    name = 'proxySpider'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nt/']
    baseUrl = "https://www.xicidaili.com"


    def parse(self, response):
        selector = Selector(response)
        for each in selector.xpath("//tr[@class='odd']"):
            item = ProxyspiderItem()
            item['type'] = each.xpath("./td[6]/text()").extract()[0]
            item['host'] = each.xpath("./td[2]/text()").extract()[0]
            item['port'] = each.xpath("./td[3]/text()").extract()[0]
            yield item

        nextUrl = self.baseUrl + selector.xpath("//a[@class='next_page']/@href").extract_first()
        if (nextUrl):
            yield Request(url=nextUrl, callback=self.parse)
