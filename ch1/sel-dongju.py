#!/usr/bin/env python
# -*- coding: utf8 -*

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlencode, quote

url = "https://ko.wikisource.org/wiki/" + quote("저자:윤동주")
print(url)
res = urlopen(url)
# print(res)
soup = BeautifulSoup(res, "html.parser")

# selector
# #mw-content-text > div > ul:nth-child(6) > li > b > a
# id가 mw-content-text 아래에 있는
# ul 태그 바로 아래에 있는
# li 태그 아래에 있는
# 모든 a 태그
a_list = soup.select("#mw-content-text > div > ul > li a")
# print(a_list)
for a in a_list:
    name = a.string
    print("-", name)