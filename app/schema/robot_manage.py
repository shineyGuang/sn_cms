# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 10:28 上午
# @Author  : ShineyZhao
# @File    : robot_manage.py
# @Email   : shiney_zhao@163.com
import uuid
from typing import Optional, List

from pydantic import BaseModel, Field


class CreateRobotModel(BaseModel):
    """
    创建机器人post提交json约束
    """
    # robot_info 表
    robot_name: Optional[str] = Field(..., max_length=50)
    download_counter: int
    image: str
    category_id: str
    publisher_id: str
    # robot_details_info 表
    details_id: str = uuid.uuid4()
    content: str = None
    cur_version: str = "v1.0.0"
    video: str = None


class RobotInfoModel(BaseModel):
    # robot_info 表
    robot_name: Optional[str] = Field(..., max_length=50)
    download_counter: int
    image: str
    category_id: str
    publisher_id: str


class RobotDetailsInfoModel(BaseModel):
    # robot_details_info 表
    details_id: str = uuid.uuid4()
    content: str = None
    cur_version: str = "v1.0.0"
    video: str = None


class EditRobotInfoModel(BaseModel):
    # robot_info 表
    robot_name: str
    download_counter: int
    image: str
    category_id: str
    publisher_id: str


class EditRobotDetailsInfoModel(BaseModel):
    # robot_details_info 表
    content: str = None
    cur_version: str
    video: str = None


class EditRobotUpdateInfoModel(BaseModel):
    # robot_update_info 表
    update_content: str = None


class EditRobotModel(BaseModel):
    robot_info: EditRobotInfoModel
    robot_details_info: EditRobotDetailsInfoModel
    robot_update_info: EditRobotUpdateInfoModel


class RobotTotalInfoModel(BaseModel):
    robot_id: str
    robot_name: str
    download_counter: str
    publisher_id: str
    category_id: str = Field(..., alias="category__category_id")
    category_name: str = Field(..., alias="category__category_name")
    details_id: str = Field(..., alias="details_robot__details_id")
    content: str = Field(..., alias="details_robot__content")
    cur_version: str = Field(..., alias="details_robot__cur_version")
    video: str = Field(..., alias="details_robot__video")


class RobotUpdateInfoOutModel(BaseModel):
    """
    updateInfo输出响应
    """
    robot_id: str
    update_id: str
    update_date: str
    update_content: str
