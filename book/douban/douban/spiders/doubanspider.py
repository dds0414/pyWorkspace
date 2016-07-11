# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.selector import Selector
from douban.items import DoubanItem
from urllib import quote, unquote

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class DoubanspiderSpider(scrapy.Spider):
    name = "doubanspider"
    allowed_domains = ["douban.com"]

    cookie = {
        'bid' : 'kF0Ww5VB3rs'
    }

    head = {
        'Host': 'www.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
    }

    def __init__(self, key=None, *args, **kwargs):
        super(DoubanspiderSpider, self).__init__(*args, **kwargs)
        self.count = 0
        v = key.split('|')
        self.key = v[0]
        self.value = v[1]
        print(self.key)

    def start_requests(self):
        return [Request("https://www.douban.com/tag/"+self.key+"/book", cookies=self.cookie, headers=self.head, callback=self.parse)]

    def parse(self, response):
        list = Selector(response).xpath('//div[@class="mod book-list"]/dl')
        for i in list:
            item = DoubanItem()
            item['title'] = i.xpath('dd/a[@class="title"]/text()').extract()[0]
            item['desc'] = i.xpath('dd/div[@class="desc"]/text()').extract()[0].replace('\n', '').strip()
            item['star'] = i.xpath('dd/div[@class="rating"]/span[2]/text()').extract()[0]
            item['key'] = self.value.decode("GBK")
            yield item
        self.count += 15
        if self.count <= 100:
            yield Request("https://www.douban.com/tag/"+self.key+"/book?start="+str(self.count)+"", headers=self.head, callback=self.parse)
