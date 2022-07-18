# coding:utf-8
from lxml import etree
import requests

url = 'https://music.douban.com/top250'

html = requests.get(url).text
s = etree.HTML(html)
href = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a/@href')[0]#因为要获取标题，所以我需要这个当前路径下的文本，所以使用/text()
title = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a/text()')[0]#因为要获取标题，所以我需要这个当前路径下的文本，所以使用/text()
score = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[2]/text()')[0]#因为要获取文本，所以我需要这个当前路径下的文本，所以使用/text()
numbers = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[3]/text()')[0]#因为要获取文本，所以我需要这个当前路径下的文本，所以使用/text()
imgpath = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[1]/a/img/@src')[0]#因为要获取文本，所以我需要这个当前路径下的文本，所以使用/text()
print(href,title,score,numbers,imgpath)