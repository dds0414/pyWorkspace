from workflow import Workflow,web,ICON_WEB


wf = Workflow()
r = web.get("http://www.wangpansou.cn/s.php?wp=0&ty=gn&op=gn&q=python&q=php")
print r.content