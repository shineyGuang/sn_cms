# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 9:38 上午
# @Author  : ShineyZhao
# @File    : category_view.py
# @Email   : shiney_zhao@163.com
import uuid

from fastapi import APIRouter, Depends

from app.core.curd import Curd
from app.extension.response.response import ResponseBaseModel
from app.extension.response.response_code import ResponseCode, ResponseMessage
from app.models import CategoryInfo
from app.schema.category_manage import CategoryModel
from app.utils.security import get_current_user

category_manager_router = APIRouter()


@category_manager_router.get("/category/queryAll", response_model=ResponseBaseModel, summary="查找所有类别")
async def get_all_category():
    category_info = await Curd(CategoryInfo).queryAll(is_del=0)
    return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, data=category_info, msg=ResponseMessage.Success)


@category_manager_router.post("/category/createOneCry", dependencies=[Depends(get_current_user)],
                              response_model=ResponseBaseModel, response_model_exclude_unset=True, summary="创建一个类别")
async def create_category(category: CategoryModel):
    await Curd(CategoryInfo).create(**category.dict(), category_id=uuid.uuid4())
    return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, msg=ResponseMessage.Success)


@category_manager_router.put("/category/editCategory/{category_name}", dependencies=[Depends(get_current_user)],
                             response_model=ResponseBaseModel,
                             response_model_exclude_unset=True,
                             summary="更新类别")
async def edit_category(category_name: str, category: CategoryModel):
    categoryObj = await Curd(CategoryInfo).querySingle(category_name=category_name, is_del=0)
    if categoryObj:
        await Curd(CategoryInfo).update({"category_id": categoryObj.category_id}, **category.dict())
        return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, msg=ResponseMessage.Success)
    return ResponseBaseModel(statusCode=ResponseCode.CATEGORY_EDIT_FAILED, msg=ResponseMessage.CategoryNotExistErr)


@category_manager_router.delete("/category/delCategory/{category_name}", dependencies=[Depends(get_current_user)],
                                response_model=ResponseBaseModel, response_model_exclude_unset=True, summary="删除类别")
async def delete_category(category_name: str):
    categoryObj = await Curd(CategoryInfo).querySingle(category_name=category_name, is_del=0)
    if categoryObj:
        await Curd(CategoryInfo).delete(category_id=categoryObj.category_id)
        return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, msg=ResponseMessage.DelCategorySuccess)
    return ResponseBaseModel(statusCode=ResponseCode.CATEGORY_NOT_FOUND, msg=ResponseMessage.DelCategoryFailed)
