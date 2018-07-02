# 默认是不能在IDE中调试的 创建这个文件的目的
from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'dingdian'])