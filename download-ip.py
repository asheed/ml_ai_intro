#!/usr/bin/env python
# -*- coding: utf8 -*

from urllib import request

url = "http://api.aoikujira.com/ip/ini"
res = request.urlopen(url)
data = res.read()

text = data.decode("utf=8")
print(text)