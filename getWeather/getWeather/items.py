# -*- coding:UTF-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class weatherItem(scrapy.Item):
    date = scrapy.Field()  # 日期
    wea = scrapy.Field()  # 天气
    tem_max = scrapy.Field()  # 最高温度
    tem_min = scrapy.Field()  # 最低温度
    wind_direction = scrapy.Field()  # 风向
    wind_level = scrapy.Field()  # 风力
