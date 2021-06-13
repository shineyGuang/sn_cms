# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 16:47
# @Author  : 20019236
# @File    : user_view.py
# @Software: fastApi_CLI-master
import time
from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.core.curd import Curd
from app.extension.response.response_code import ResponseCode, ResponseMessage
from app.models.base_model import UserInfo, RobotInfo
from app.extension.response.response import ResponseBaseModel

from app.schema.user_manage import LoginUserRes, UserTokenRes, Token, UserEditModel, UserOutModel
from app.utils import security
from app.utils.customer_exc import TokenAuthError
from app.utils.security import check_password_hash, create_access_token, generate_password_hash, get_current_user
from config import configs

user_manager_router = APIRouter()

UserQueryModel = pydantic_model_creator(UserInfo, name="ClientUser")
UserInQueryModel = pydantic_model_creator(UserInfo, name="ClientUserIn", exclude_readonly=True)


@user_manager_router.post("/register", response_model=ResponseBaseModel, response_model_exclude_unset=True,
                          summary="用户注册")
async def register_user(user: UserInQueryModel):
    # 先查一下是否存在
    user_info = user.dict()
    try:
        if await UserQueryModel.from_queryset_single(UserInfo.get(auth_user_id=user_info.get("auth_user_id"))):
            return ResponseBaseModel(statusCode=ResponseCode.HTTP_400_BAD_REQUEST, msg=ResponseMessage.UserIsExistsErr)
    except Exception as e:
        user_info["password_hash"] = generate_password_hash(user_info["password_hash"])
        await UserInfo.create(**user_info)
        return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, data=UserOutModel(**user_info),
                                 msg=ResponseMessage.Success)


@user_manager_router.post('/login/access-token', response_model=Token, status_code=status.HTTP_201_CREATED)
async def login_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """OAuth2 compatible token login, get an access token for future requests"""
    # user = crud.user.authenticate(
    #     db=db,
    #     username=form_data.username,
    #     password=form_data.password
    # )
    userObj = await UserInfo.filter(auth_user_id=form_data.username).first()
    if not userObj:
        raise TokenAuthError()
    access_token_expires = timedelta(minutes=configs.ACCESS_TOKEN_EXPIRE_MINUTES)
    user_sign = {
        "time_stamp": int(time.time()),
        "username": userObj.username,
        "auth_user_id": userObj.auth_user_id,
    }
    return {
        'access_token': security.create_access_token(
            user_sign, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }


@user_manager_router.post("/login", response_model=ResponseBaseModel, response_model_exclude_unset=True, summary="用户登录")
async def user_login(user: LoginUserRes):
    userObj = await UserInfo.filter(auth_user_id=user.user_id).first()
    if not userObj:
        return ResponseBaseModel(statusCode=ResponseCode.HTTP_401_UNAUTHORIZED, msg=ResponseMessage.NotFondUserErr)
    if not check_password_hash(userObj.password_hash, user.password):
        return ResponseBaseModel(statusCode=ResponseCode.HTTP_401_UNAUTHORIZED, msg=ResponseMessage.PasswordErr)
    user_sign = {
        "time_stamp": int(time.time()),
        "username": userObj.username,
        "auth_user_id": userObj.auth_user_id,
    }
    # 生成token
    token = create_access_token(subject=user_sign)
    # 查找关联的机器人
    userObj_robot_info = await RobotInfo.filter(publisher_id=user.user_id).all().values(
        "robot_id", "robot_name", "image", "download_counter", "category__category_name"
    )
    return ResponseBaseModel(
        statusCode=ResponseCode.HTTP_200_OK,
        data=UserTokenRes(
            user_id=user.user_id,
            token=token,
            user_robot=userObj_robot_info
        ),
        msg=ResponseMessage.LoginSuccess
    )


@user_manager_router.get("/user/queryAll", dependencies=[Depends(get_current_user)], response_model=ResponseBaseModel,
                         response_model_exclude_unset=True, summary="查看所有用户")
async def get_all_users():
    user_info = await UserInfo.filter(is_del=0).all().values("auth_user_id", "username")
    if user_info:
        return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, data=user_info,
                                 msg=ResponseMessage.Success)
    return ResponseBaseModel(statusCode=ResponseCode.USER_NOT_EXIST, msg=ResponseMessage.NotFondUserErr)


@user_manager_router.get("/user/getOneUser/{auth_user_id}", dependencies=[Depends(get_current_user)],
                         response_model=ResponseBaseModel, response_model_exclude_unset=True, summary="查找单个用户")
async def get_one_user(auth_user_id: str):
    user_info = await UserInfo.filter(auth_user_id=auth_user_id, is_del=0).first().values("auth_user_id", "username")
    if user_info:
        return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, data=user_info,
                                 msg=ResponseMessage.Success)
    return ResponseBaseModel(statusCode=ResponseCode.USER_NOT_EXIST, msg=ResponseMessage.NotFondUserErr)


@user_manager_router.put("/user/editUser/{auth_user_id}", dependencies=[Depends(get_current_user)],
                         response_model=ResponseBaseModel, response_model_exclude_unset=True, summary="更新用户")
async def edit_user(auth_user_id: str, user: UserEditModel):
    user_info = await Curd(UserInfo).querySingle(is_del=0, auth_user_id=auth_user_id)
    if not user_info:
        return ResponseBaseModel(statusCode=ResponseCode.USER_NOT_EXIST, msg=ResponseMessage.NotFondUserErr)
    await Curd(UserInfo).update({"is_del": 0, "auth_user_id": auth_user_id}, username=user.dict().get("username"),
                                password_hash=generate_password_hash(user.dict().get("password")))
    return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, msg=ResponseMessage.Success)


@user_manager_router.delete("/user/deleteUser/{auth_user_id}", dependencies=[Depends(get_current_user)],
                            response_model=ResponseBaseModel, response_model_exclude_unset=True, summary="注销用户")
async def delete_user(auth_user_id: str):
    user_info = await Curd(UserInfo).querySingle(is_del=0, auth_user_id=auth_user_id)
    if not user_info:
        return ResponseBaseModel(statusCode=ResponseCode.USER_NOT_EXIST, msg=ResponseMessage.NotFondUserErr)
    await Curd(UserInfo).delete(is_del=0, auth_user_id=auth_user_id)
    return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, msg=ResponseMessage.Success)
