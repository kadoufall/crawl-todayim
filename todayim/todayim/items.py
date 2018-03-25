# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TodayimItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsItem(scrapy.Item):
    url = scrapy.Field()
    loc = scrapy.Field()
    title = scrapy.Field()
    postTime = scrapy.Field()
    commentNum = scrapy.Field()
    viewNum = scrapy.Field()
    className = scrapy.Field()
    passageContent = scrapy.Field()
