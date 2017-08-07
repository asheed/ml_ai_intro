#!/usr/bin/env python
# -*- coding: utf8 -*

from urllib.request import urlopen
from urllib.parse import urlencode

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId': '108'
}

params = urlencode(values)

url = API + "?" + params
print("url=", url)

# 다운로드
data = urlopen(url).read()
text = data.decode('utf-8')
print(text)