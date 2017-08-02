#!/usr/bin/env python
#-*- coding: utf-8 -*-

from urllib import request

url = "http://imgnews.naver.net/image/413/2017/07/13/0000052580_001_20170713163927829.jpg"
savename = "heungmin.jpg"

# 다운로드
request.urlretrieve(url, savename)

print("파일이 저장되었습니다.")