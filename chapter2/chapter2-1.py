# -*- coding:UTF-8 -*-
import requests

# Author:Linghu Feixia
# Date:2019-12-9

response1 = requests.get(url='http://www.baidu.com')
# 打印返回状态码
print(response1.status_code)


# 设置代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
response2 = requests.get(url='http://www.baidu.com', headers=headers)
# 返回状态码
print(response2.status_code)

# 输出编码规则
print(response2.encoding)
# 输出header
#print(response2.headers)
# 输出response的文本
print(response2.text)

