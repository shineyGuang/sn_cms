# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 14:14
# @Author  : 20019236
# @File    : catch.py
# @Software: fastApi_CLI-master
import logging
import traceback

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.extension.response.response_code import ResponseMessage
from app.utils.customer_exc import PostParamsError, TokenAuthError


logger = logging.getLogger(__name__)


def register_exception(app: FastAPI):
    """
    全局异常捕获
    :param app:
    :return:
    """

    # 捕获自定义异常
    @app.exception_handler(PostParamsError)
    async def query_params_exception_handler(request: Request, exc: PostParamsError):
        """
        捕获 自定义抛出的异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"参数查询异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"statusCode": 400, "data": None, "msg": exc.err_desc},
        )

    @app.exception_handler(TokenAuthError)
    async def token_exception_handler(request: Request, exc: TokenAuthError):
        logger.error(f"参数查询异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"statusCode": 400, "data": None, "msg": exc.err_desc},
        )

    # 捕获参数 验证错误
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        捕获请求参数 验证错误
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"参数错误\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({"statusCode": 400, "data": None, "msg": ResponseMessage.InvalidParameter}),
        )

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(f"全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"statusCode": 500, "data": None, "msg": ResponseMessage.NoResourceFound},
        )
