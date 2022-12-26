"""
抓取信息导出CSV文件

"""
import random

import requests
from lxml import etree
import csv
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}


def get_request(pages):
    url = 'https://www.spinics.net/lists/kernel/mail'

    proxy = '127.0.0.1:7890'
    proxies = {
        "http": "http://%(proxy)s/" % {'proxy': proxy},
        "https": "http://%(proxy)s/" % {'proxy': proxy}
    }

    for page in range(2, pages+1): #pages+1
        time.sleep(random.random())
        url1 = url + str(page) + ".html"
        resp = requests.get(url1, headers=header, proxies=proxies)
        print('正在获取第 %s 页邮件列表！' % page)
        if resp.status_code == 200:
            parse_html(resp.text)
        else:
            print("请求失败！")


def parse_html(html):
    root = etree.HTML(html)
    items = root.xpath('/html/body/ul[2]/li/strong/a/text()')
    itempipe4csv(items)


def itempipe4csv(items):
    #保存到csv


if __name__ == '__main__':
    get_request(100)


