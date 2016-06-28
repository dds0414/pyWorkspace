# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.wangpansou.cn/s.php?wp=0&ty=gn&op=gn&q=python&q=php')
res = BeautifulSoup(r.content)
for i in res.find_all("a", class_="cse-search-result_content_item_top_a"):
    print i.text.encode('utf-8').strip(), i.attrs['href']