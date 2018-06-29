# coding: utf-8

import requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url,  headers=headers)
print(start_html.text)


soup = BeautifulSoup(start_html.text,'lxml')


all_li = soup.find


