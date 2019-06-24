# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    areas = scrapy.Field()
    title = scrapy.Field()
    listing_time = scrapy.Field()

    prices = scrapy.Field()
    price = scrapy.Field()
    hou = scrapy.Field()
    # room = scrapy.Field()
    # hall = scrapy.Field()
    # toilet = scrapy.Field()
    area = scrapy.Field()
    orient = scrapy.Field()

    flo = scrapy.Field()
    # floor = scrapy.Field()
    # floors = scrapy.Field()
    fitment = scrapy.Field()
    elevator = scrapy.Field()
    address = scrapy.Field()
    coordinate = scrapy.Field()

    coordinate_type = scrapy.Field()
    build_type = scrapy.Field()
    build_time = scrapy.Field()
    crawl_time = scrapy.Field()
    quanshu = scrapy.Field()
    pass

class LianjiaZFItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    areas = scrapy.Field()
    address = scrapy.Field()
    avg_price = scrapy.Field()
    num_moufinish = scrapy.Field()
    num_listings = scrapy.Field()
    num_rents = scrapy.Field()
    num_buildings = scrapy.Field()
    num_houses = scrapy.Field()
    build_type = scrapy.Field()
    build_time = scrapy.Field()
    developers = scrapy.Field()
    crawl_time = scrapy.Field()
