# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DemoPipeline(object):
    def process_item(self, item, spider):
        return item
class BaidustocksInfoPipline(object):

    def open_spider(self, spider):
        self.f = open('Baidustockinfo.txt', 'w')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = str(dict[item]) + "\n"
            self.f.write(line)
        except:
            pass
        return item


