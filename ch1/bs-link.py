#!/usr/bin/env python
# -*- coding: utf8 -*

from bs4 import BeautifulSoup
html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

# HTML 분석
soup = BeautifulSoup(html, 'html.parser')

# find_all() 메서드로 추출
links = soup.find_all("a")
print(links)
print(type(links))
# 링크 목록 출력하기
for a in links:
    print(type(a))
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)