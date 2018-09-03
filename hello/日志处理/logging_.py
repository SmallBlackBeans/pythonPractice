import logging

"""
%(levelno)s：打印日志级别的数值。
%(levelname)s：打印日志级别的名称。
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]。
%(filename)s：打印当前执行程序名。
%(funcName)s：打印日志的当前函数。
%(lineno)d：打印日志的当前行号。
%(asctime)s：打印日志的时间。
%(thread)d：打印线程ID。
%(threadName)s：打印线程名称。
%(process)d：打印进程ID。
%(processName)s：打印线程名称。
%(module)s：打印模块名称。
%(message)s：打印日志信息。
"""
logging.basicConfig(level=logging.DEBUG,
                    filename='output.log',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s'
                    )
logger = logging.getLogger(__name__)

# 单独设置
logger.setLevel(level=logging.DEBUG)
handler = logging.FileHandler('output.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


from logging.handlers import HTTPHandler
import sys
#  输出handler
# StreamHandler 日志输出到流
# stream_handler = logging.StreamHandler(sys.stdout)
# stream_handler.setLevel(level=logging.DEBUG)
# logger.addHandler(stream_handler)
#
# # FileHandler 日志输出到文件
# file_handler = logging.FileHandler('output.log')
# file_handler.setLevel(level=logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
#
# # HTTPHandler 日志输出到远程
# http_handler = HTTPHandler(host='localhost:8001', url='log', method='POST')
# logger.addHandler(http_handler)
#
#
# logger.info('This is a log info')
# logger.debug('Debugging')
# logger.warning('Warning')
# logger.error('Error exsits')


"""捕获 Traceback"""

logger.info('start')
logger.warning('Something maybe fail')
try:
    result = 10 / 0
except Exception:
    logger.error('Faild to get result',exc_info=True)
logger.info('Finished')



import core
logger = logging.getLogger('main')
core.run()














