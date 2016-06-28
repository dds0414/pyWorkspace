# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

r = requests.get('http://www.baidu.com/s?wd=python')
res = BeautifulSoup(r.content)
for i in res.find_all("h3", class_="t"):
    res = re.findall(r".*?href=\"(http://www.baidu.com/link.*?)\".*?target=\"_blank\"\>(.*?)<\/a>", str(i))
    if(res):
        print res[0][1].replace("<em>", "").replace("</em>", "")
