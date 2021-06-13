# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 10:26 下午
# @Author  : ShineyZhao
# @File    : __init__.py.py
# @Email   : shiney_zhao@163.com
import logging

from fastapi import FastAPI

from app.extension.catch import register_exception
from app.extension.logger import log_init, logger
from app.extension.middleware import middleware_init
from app.mydbs.database import db_init
from app.routers import router_init
from app.utils.common_util import write_log


def conf_init(app):
    from config import configs
    if configs.ENVIRONMENT == 'production':
        app.docs_url = None
        app.redoc_url = None
        app.debug = False


# async def start_event():
#     await write_log(msg='系统启动')
#
#
# async def shutdown_event():
#     await write_log(msg='系统关闭')


def create_app():
    app = FastAPI(
        title="SN_CMS",
        description="CMS平台用户模块接口文档",
        version="basic.0.0",
        # on_startup=[start_event],
        # on_shutdown=[shutdown_event]
    )

    # 日志
    log_init()
    logger.info("日志启动成功！")

    # 注册全局异常捕获
    register_exception(app)
    logger.info("异常捕获启动成功！")

    # 加载配置
    conf_init(app)
    logger.info("配置加载成功！")

    # 初始化路由配置
    router_init(app)
    logger.info("路由注册成功！")

    # 初始化中间件
    middleware_init(app)
    logger.info("中间件注册成功")

    # 建表
    db_init(app)

    # 响应拦截
    # response_intercept_init(app)

    return app
