#!/usr/bin/env python
# -*- coding: utf8 -*
from bs4 import BeautifulSoup

fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

# CSS 선택자로 추출하기
print(soup.select_one("li:nth-of-type(8)").string)  # 8번째 li요소
print(soup.select_one("#ve-list > li:nth-of-type(4)").string) # id가 ve-list인 요소 바로 아래에 있는 li 태그 중 4번째 요소
print(soup.select("#ve-list > li[data-lo='us']")[1].string) # id가 ve-list인 요소 바로 아래에 있는 li 태그 중 data-lo 속성이 "us"인 것을 모두 추출하고, 그중에서 [1](0부터 세므로 2번째 요소)인 요소를 추출
print(soup.select("#ve-list > li.black")[1].string) # id가 ve-list인 요소 바로 아래에 있는 li요소 중 class 속성이 black 인것 중 두번째 요소를 추출

# find 메서드로 추출
cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)
print(soup.find(id="ve-list").find("li", cond).string)