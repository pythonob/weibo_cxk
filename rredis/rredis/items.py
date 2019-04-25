# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RredisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    u_id = scrapy.Field()
    u_name = scrapy.Field()
    gender = scrapy.Field()
    fwd_text = scrapy.Field()
    follows = scrapy.Field()
    followers = scrapy.Field()
    device = scrapy.Field()
    desc = scrapy.Field()
    fwd_id = scrapy.Field()
    pass
