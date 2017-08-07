#!/usr/bin/env python
# -*- coding: utf8 -*

from bs4 import BeautifulSoup
from re import compile

html = """
    <ul>
        <li><a href="hoge.html">hoge</a></li>
        <li><a href="https://example.com/fuga">fuga*</a></li>
        <li><a href="https://example.com/foo">foo*</a></li>
        <li><a href="http://example.com/aaa">aaa</a></li>
    </ul>
"""

soup = BeautifulSoup(html, "html.parser")

# 정규 표현식으로 href에서 https인 것 추출하기
li = soup.find_all(href=compile(r"^https://"))
for e in li:
    print(e.attrs['href'])