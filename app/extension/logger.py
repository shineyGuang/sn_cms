# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 15:14
# @Author  : 20019236
# @File    : logger.py
# @Software: fastApi_CLI-master
import logging
from logging import handlers


logger = logging.getLogger('ZcgServer_CMS')
logger.setLevel(level=logging.DEBUG)


def log_init():
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter(
        '进程ID:%(process)d - '
        '线程ID:%(thread)d- '
        '日志时间:%(asctime)s - '
        '代码路径:%(pathname)s:%(lineno)d - '
        '日志等级:%(levelname)s - '
        '日志信息:%(message)s'
    )
    logger.handlers.clear()
    file_handler = handlers.TimedRotatingFileHandler(r'logs/ZcgServerCMS.log', encoding='utf-8', when='W6')
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
