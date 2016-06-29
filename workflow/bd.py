# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

r = requests.get('http://www.baidu.com/s?wd=python')
res = BeautifulSoup(r.content, "lxml")

# for i in res.find_all("h3", class_="t"):
#     res = re.findall(r".*?href=\"(http://www.baidu.com/link.*?)\".*?target=\"_blank\"\>(.*?)<\/a>", str(i))
#     if(res):
#         print res[0][1].replace("<em>", "").replace("</em>", "")
url = 'https://www.baidu.com'
icon = 'icon.png'
print "<?xml version=\"1.0\"?>\n<items>"
if(res.find_all("h3", class_="t")):
    for item in res.find_all("h3", class_="t"):
        res = re.findall(r".*?href=\"(http://www.baidu.com/link.*?)\".*?target=\"_blank\"\>(.*?)<\/a>", str(item))
        if(res):
            title = res[0][1].replace("<em>", "").replace("</em>", "")
            subtitle = ""
            link = res[0][0]
            print "<item uid=\"smzds"+link+"\" arg=\""+ link +"\">"
            print "    <title>" + title + "</title>"
            print "    <subtitle>" + subtitle.encode('utf-8')+ "</subtitle>"
            print "    <icon type=''>"+icon+"</icon>"
            print "</item>"
else:
        print "<item uid=\"smzds\" arg=\""+ url +"\">"
        print "    <title>暂无结果</title>"
        print "    <subtitle></subtitle>"
        print "    <icon type=''>"+icon+"</icon>"
        print "</item>"

print "</items>\n"