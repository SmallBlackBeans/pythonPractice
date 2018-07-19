from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')
# 获取部署的所有项目
print(scrapyd.list_projects())