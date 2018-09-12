# 设置中文编码
# coding=utf-8
# 引入网络模块
import requests
import json
import math
import os
# 输出当前模块内容
# print(dir(requests), end="\n")
heads = {
    'Referer': 'https://www.bilibili.com/anime/index/',
    'Origin': 'http://bangumi.bilibili.com',
    'Host': 'bangumi.bilibili.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.9 Safari/537.36',
}
proxies = {
    'http': 'https://115.239.210.27'
}
num = 1
url = 'https://bangumi.bilibili.com/media/web_api/search/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&pub_date=-1&style_id=-1&order=3&st=1&sort=0&season_type=1&pagesize=20&page=' + str(num)

# 读取数据
request = requests.get(url, headers = heads, proxies = proxies, timeout = 600)
dictData = json.loads(request.text)
data = dictData['result']['page']
print(dictData['result']['data'])

# 计算需要爬取多少页
size = data['size']
total = data['total']
totalPage = math.ceil(total / size)

path = os.getcwd()
file = open(path + '\\index.txt', 'w+', encoding = 'utf8')

def spider (url):
    request = requests.get(url)
    dictData = json.loads(request.text)
    
    string = str(dictData['result']['data'])
    file.write(string)

for i in range(1, totalPage + 1):
    spider('https://bangumi.bilibili.com/media/web_api/search/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&pub_date=-1&style_id=-1&order=3&st=1&sort=0&season_type=1&pagesize=20&page=' + str(i))
    print(i)