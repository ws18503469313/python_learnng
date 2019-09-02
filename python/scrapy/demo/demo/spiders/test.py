# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    # allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        fname = response.url.split("/")[-1]
        with open (fname, 'wb') as f:
            f.write(response.body)
            f.close()
        self.log("saved file{:^20}".format(fname))
        pass
