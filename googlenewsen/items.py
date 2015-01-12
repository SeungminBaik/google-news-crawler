# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GooglenewsenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # any additional information needed? publisher? section?
    title = scrapy.Field()
    image = scrapy.Field()
    desc = scrapy.Field()