
import sys
from workflow import Workflow, ICON_WEB, web

def mainFunction(wf):
    url = u"http://www.wangpansou.cn/s.php?wp=0&ty=gn&op=gn&q=&q=a"
    param = dict(wp=0, ty='gn', op='gn', q='json')




if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(mainFunction))