# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 10:22
# @Author  : 20019236
# @File    : test_manager.py
# @Software: fastApi_CLI-master
import logging
from typing import List, Optional, Any

from fastapi import APIRouter
from pydantic import BaseModel

logger = logging.getLogger(__name__)

test_manage_router = APIRouter()


@test_manage_router.get("/test")
async def get_test():
    logger.info("测试成功")
    return {
        "statusCode": 200,
        "data": {
            "key1": "v1",
            "key2": "v2"
        },
        "msg": "测试成功"
    }


class ResponseBaseModel(BaseModel):
    statusCode: int
    data: Optional[Any] = None
    msg: str

# class GetUsersResponseModel(ResponseBaseModel):
#     data: List[UserQueryModel] = []
#
#
# @test_manage_router.get("/users", response_model=ResponseBaseModel)
# async def get_users():
#     logger.info("getUser成功")
#     data = await UserQueryModel.from_queryset(UserInfo.all())
#     return ResponseBaseModel(statusCode=200, data=data, msg="GetUser Success")
#
#
# @test_manage_router.get("/user/{user_id}", response_model=ResponseBaseModel)
# async def get_one_user(user_id: int):
#     data = await UserQueryModel.from_queryset_single(UserInfo.get(id=user_id))
#     return ResponseBaseModel(statusCode=200, data=data, msg="GetOneUser Success")
