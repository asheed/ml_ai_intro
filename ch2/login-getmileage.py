#!/usr/bin/env python
# -*- coding: utf8 -*

# 로그인을 위한 모듈
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호 지정
USER = "asheed77"
PASS = "ashe1#go"

# 세션 시작
session = requests.session()
# 로그인
login_info = {
	"m_id" : USER,      # 아이디
	"m_passwd" : PASS   # 비밀번호
}
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() # 오류가 발생하면 예외를 발생합니다.

# 마이페이지로 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()
#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span
# 마일리지와 이코인 가져오기
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지: " + mileage)
print("이코인: " + ecoin)