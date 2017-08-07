#!/usr/bin/env python
# -*- coding: utf8 -*

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# urlopen()으로 데이터 수집
res = urlopen(url)

# BeautifulSoup 으로 분석
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)