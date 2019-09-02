# -*- coding: utf-8 -*-
import scrapy
import re

class StocksSpider(scrapy.Spider):
    name = 'stocks'
    # allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for a in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][hz]\d{6}', a)[0]
                url = "https://gupiao.baidu.com/stock/" + stock + '.html'
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue
        pass
    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css('stock-bets')
        name = stockInfo.css('bets-name').extract()[0]
        keylist = stockInfo.css('dt').extract()
        valuelist= stockInfo.css('dd').extract()
        for i in range(len(keylist)):
            key = re.findall(r'>.*</dt>', keylist[i])[0][1:5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valuelist[i])[0][0:5]
            except:
                val = "--"
            infoDict[key] = val
        infoDict.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + \
             re.findall('\>.*\<', name)[0][1: -1]}
        )
        yield
