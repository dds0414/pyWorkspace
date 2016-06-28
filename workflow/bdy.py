# -*- coding: utf-8 -*-
from workflow import web, Workflow, ICON_WEB
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def m(wf):
    r = web.get('http://www.wangpansou.cn/s.php?wp=0&ty=gn&op=gn&q=python&q=php')
    res = BeautifulSoup(r.content, "lxml")
    for item in res.find_all("a", class_="cse-search-result_content_item_top_a"):
        wf.add_item(title=item.text.encode('utf-8').strip(),
                    subtitle=item.attrs['href'],
                    arg=item.attrs['href'],
                    icon=ICON_WEB,
                    valid=True)

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(m))
