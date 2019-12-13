# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

# Author:Linghu Feixia
# Date:2019-12-10

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
reponse1 = requests.get(url='http://www.weather.com.cn/weather/101010100.shtml', headers=headers)
reponse1.encoding = 'UTF8'
# 产生异常信息
reponse1.raise_for_status()

demo = reponse1.text
bsoup = BeautifulSoup(demo, 'html.parser')

# 美化HTML代码显示
#print(bsoup.prettify())

weathers = bsoup.find_all('li', class_='sky skyid lv2 on')
#print(weathers)

for weather in weathers:
    print("---------天气预报------------")

    # 获取日期
    date = weather.find('h1').text
    print("日期:", end=" ")
    print(date)

    # 获取天气
    wea = weather.find('p', class_='wea').text
    print("天气:", end=" ")
    print(wea)

    # 获取风向\风力
    windP = weather.find('p', class_='win')
    windDirections = windP.find_all('span')
    for windDirection in windDirections:
        print(windDirection)
        print("风向:", end=" ")
        print(windDirection.attrs.get('title'))

    windLevel = windP.find('i').text
    print("风力:", end=" ")
    print(windLevel)

    # 获取温度
    tem_p = weather.find('p', class_='tem')
    tem_min = tem_p.find('i').text
    print("最低温度:", end=" ")
    print(tem_min)
    tem_span = tem_p.find('span')
    if tem_span is not None:
        tem_max = tem_span.text
        print("最高温度:", end=" ")
        print(tem_max)
