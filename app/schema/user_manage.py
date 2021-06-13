# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 19:05
# @Author  : 20019236
# @File    : user_manage.py
# @Software: fastApi_CLI-master
from typing import Optional, Union, List, Dict

from pydantic import BaseModel, Field


class LoginUserRes(BaseModel):
    user_id: str
    password: str


class UserRobotInfo(BaseModel):
    robot_id: str
    robot_name: str
    download_counter: str
    image: Union[str, None]
    category_id: str


class UserTokenRes(BaseModel):
    user_id: str
    user_robot: List[Dict]
    token: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserOutModel(BaseModel):
    username: str
    auth_user_id: int


class UserEditModel(BaseModel):
    username: str
    password: str = Field(..., min_length=6, max_length=30)
