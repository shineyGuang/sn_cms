# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 16:54
# @Author  : 20019236
# @File    : response.py
# @Software: fastApi_CLI-master
from typing import Optional, Any, List

from fastapi import Body
from pydantic import BaseModel, Field


class ResponseBaseModel(BaseModel):
    statusCode: int = None
    data: Optional[Any] = None
    msg: str = None
