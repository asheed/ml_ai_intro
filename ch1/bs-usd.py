#!/usr/bin/env python
# -*- coding: utf8 -*

from bs4 import BeautifulSoup
from urllib.request import urlopen

# HTML 가져오기
url = "http://info.finance.naver.com/marketindex/"
res = urlopen(url)

# HTML  분석
soup = BeautifulSoup(res, "html.parser")

# 데이터 추출
price = soup.select_one("div.head_info > span.value").string
percent = soup.select_one("div.head_info > span.change").string
if float(percent) >= 0:
    mark = '▲'
else:
    mark = '▼'
print("usd/krw = {} 원 ({} {} %)".format(price, mark, percent))
