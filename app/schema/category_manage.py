# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 9:42 上午
# @Author  : ShineyZhao
# @File    : category_manage.py
# @Email   : shiney_zhao@163.com
from pydantic import BaseModel


class CategoryModel(BaseModel):
    category_name: str
