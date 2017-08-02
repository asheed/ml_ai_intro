#!/usr/bin/env python
# -*- coding: utf8 -*

import sys
from urllib.request import urlopen
from urllib.parse import urlencode

# 명령줄 매개변수 추출
if len(sys.argv) <= 1:
    print("사용법: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

# 매개변수를 URL 인코딩
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = urlencode(values)
url = API + "?" + params
print("url=", url)

# 다운로드
data = urlopen(url).read()
text = data.decode('utf-8')
print(text)