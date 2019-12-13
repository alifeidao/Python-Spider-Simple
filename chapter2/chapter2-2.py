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

reponse_text = reponse1.text
bsoup = BeautifulSoup(reponse_text, 'html.parser')

head= bsoup.head
print("head标签:")
print(head)

p=bsoup.p
print("第一个P标签:")
print(p)

print("父节点:")
print(p.parent)

print("对标签的直接子节点进行循环:")
body = bsoup.find("div",class_='body')
for child in p.children:
    print(child)

