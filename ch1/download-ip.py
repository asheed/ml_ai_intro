#!/usr/bin/env python
# -*- coding: utf8 -*

from urllib.request import urlopen
from requests import HTTPError

try:
    url = "http://api.aoikujira.com/ip/ini"
    res = urlopen(url)
except HTTPError as e:
    res = e.read()

data = res.read()

text = data.decode("utf=8")
print(text)