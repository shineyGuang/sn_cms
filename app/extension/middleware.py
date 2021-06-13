# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 15:18
# @Author  : 20019236
# @File    : middleware.py
# @Software: fastApi_CLI-master
import logging

from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from config import configs

logger = logging.getLogger(__name__)

# 指定允许跨域请求的url
origins = [
    "*"
]


def middleware_init(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# def response_intercept_init(app):
#     @app.middleware("http")
#     async def logger_request(request: Request, call_next):
#         # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
#         # print(request.headers.get("authorization"), type(request.headers.get("authorization")))
#         if request.url.path not in configs.WIGHT_LIST and not request.headers.get("authorization"):
#             logger.info(f"\n访问记录:{request.method}\nUrl:{request.url}\nHeaders:{request.headers.get('user-agent')}"
#                         f"\nIP:{request.client.host}\nPath:{request.url.path}\n未授权!")
#             return {"statusCode": 400, "data": None, "msg": "未授权！"}
#
#         response = await call_next(request)
#
#         return response
