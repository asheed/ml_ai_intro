#!/usr/bin/env python
# -*- coding: utf8 -*

from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
    <h1 id='title'>스크레이핑이란?</h1>
    <p id='body'>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# HTML 분석
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출
title = soup.find(id='title')
body = soup.find(id='body')

# 텍스트 부분 출력하기
print(title)
print("#title = " + title.string)
print("#body = " + body.string)