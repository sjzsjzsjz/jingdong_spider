# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode,quote
from jingdong_spider.items import JingdongSpiderItem


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['search.jd.com']
    start_urls = ['http://search.jd.com/']
    base_url = "https://search.jd.com/Search?"
    word = "python"

    def start_requests(self):
        for page in range(1,3,2):
            param = {
                "keyword": quote(self.word),
                "enc":"utf - 8",
                "qrst":"1",
                "rt":"1",
                "stop":"1",
                "vt":"2",
                "page":"3",
                "s":"58",
                "click":"0"
            }
            url = self.base_url+urlencode(param)
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        item = JingdongSpiderItem()
        q = response.css(".gl-i-wrap")
        for i in q:
            item["name"] = i.css(".p-name a em::text").extract_first()
            item["price"] = i.css(".p-price strong i::text").extract_first()
            yield item
