#!/usr/bin/env python
#-*- coding: utf-8 -*-

from urllib.request import urlopen

url = "http://imgnews.naver.net/image/413/2017/07/13/0000052580_001_20170713163927829.jpg"
savename = "heungmin1.jpg"

# 다운로드
mem = urlopen(url).read()

# 파일로 저장
with open(savename, mode='wb') as f:
    f.write(mem)
    print("파일이 저장되었습니다.")