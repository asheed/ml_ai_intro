#!/usr/bin/env python
# -*- coding: utf8 -*

from selenium import webdriver

url = "http://www.naver.com"

browser = webdriver.Chrome('D:/DevTools/chromedriver')
browser.implicitly_wait(3)
browser.get(url)
browser.save_screenshot("Website.png")
browser.quit()