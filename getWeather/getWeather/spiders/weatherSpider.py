# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from scrapy.http import Response
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from getWeather.items import weatherItem


class weatherSpider(CrawlSpider):
    name = 'weatherSpider'
    allowed_domains = ['www.weather.com.cn']
    start_urls = ['http://www.weather.com.cn/weather/101010100.shtml']

    def parse(self, response):
        print("parse begin")
        item = weatherItem()
        selector = Selector(response)
        weathers = selector.xpath('//*[@id="7d"]/ul/li')
        for weather in weathers:
            date = weather.xpath('h1/text()').extract()[0]
            print(date)
            item['date'] = date
            wea = weather.xpath('p[1]/text()').extract()[0]
            print(wea)
            item['wea'] = wea
            tem_max = weather.xpath('p[2]/span/text()').extract()[0]
            if tem_max is not None:
                print(tem_max)
                item['tem_max'] = tem_max
            tem_min = weather.xpath('p[2]/i/text()').extract()[0]
            print(tem_min)
            item['tem_min'] = tem_min
            win_level = weather.xpath('p[3]/i/text()').extract()[0]
            print(win_level)

            win_direction = weather.xpath('p[3]/em/span[1]/@title').extract()[0]
            print(win_direction)
            yield item

        print("parse end")

        # 数据存储
        pass
