# -*- coding: utf-8 -*-

"""
    @Time    : 2018/8/21 上午11:03
    @Author  : hanxiaocu
    @File    : store.py

    日志工具
"""

import os
import logging
import time


class UtilLogger(object):
    """
        日志工具类
    """

    def __init__(self, name, logfile_name=None, level=logging.DEBUG):
        self.level = level
        self.logfile_name = logfile_name
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
        ch = None
        if logfile_name is None:
            ch = logging.StreamHandler()
        else:
            logDir = os.path.dirname(logfile_name)
            if logDir != "" and not os.path.exists(logDir):
                os.mkdir(logDir)
                pass
            now = time.localtime()
            suffix = '.%d%02d%02d' % (now.tm_year, now.tm_mon, now.tm_mday)
            ch = logging.FileHandler(logfile_name + suffix)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def set_level(self, level):
        if level.lower() == "debug":
            self.logger.setLevel(logging.DEBUG)
        elif level.lower() == "info":
            self.logger.setLevel(logging.INFO)
        elif level.lower() == "warning":
            self.logger.setLevel(logging.WARNING)
        elif level.lower() == "error":
            self.logger.setLevel(logging.ERROR)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
