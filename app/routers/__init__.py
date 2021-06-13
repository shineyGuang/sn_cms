# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 10:48 下午
# @Author  : ShineyZhao
# @File    : __init__.py.py
# @Email   : shiney_zhao@163.com
from app.api.v1.category_manager.category_view import category_manager_router
from app.api.v1.robot_manager.robot_view import robot_manager_router
from app.api.v1.test_manager.test_view import test_manage_router
from app.api.v1.user_manager.user_view import user_manager_router
from config import configs


def router_init(app):
    app.include_router(
        test_manage_router,
        prefix=configs.API_V1_STR,
        tags=["测试"],
        # dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )
    app.include_router(
        user_manager_router,
        prefix=configs.API_V1_STR,
        tags=["用户管理"],
        responses={404: {"description": "Not found"}}
    )
    app.include_router(
        robot_manager_router,
        prefix=configs.API_V1_STR,
        tags=["机器人管理"],
        responses={404: {"description": "Not found"}}
    )
    app.include_router(
        category_manager_router,
        prefix=configs.API_V1_STR,
        tags=["机器人分类管理"],
        responses={404: {"description": "Not found"}}
    )
