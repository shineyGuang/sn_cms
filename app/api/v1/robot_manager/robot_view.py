# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 14:38
# @Author  : 20019236
# @File    : robot_view.py
# @Software: fastApi_CLI-master
import datetime
import uuid

from fastapi import APIRouter, Depends

from app.core.curd import Curd
from app.extension.response.response import ResponseBaseModel
from app.extension.response.response_code import ResponseCode, ResponseMessage
from app.models import RobotInfo, RobotDetailsInfo, RobotUpdateInfo
from app.schema.robot_manage import CreateRobotModel, RobotInfoModel, RobotDetailsInfoModel, EditRobotModel, \
    RobotTotalInfoModel, RobotUpdateInfoOutModel
from app.utils.security import get_current_user

robot_manager_router = APIRouter()


@robot_manager_router.get("/robot/getAllRobot", response_model=ResponseBaseModel, summary="查找所有机器人")
async def get_all_robot():
    """
    获取所有机器人
    """
    all_robot_info = await Curd(RobotInfo).queryAll(is_del=0)
    return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, data=all_robot_info, msg=ResponseMessage.Success)


@robot_manager_router.get("/robot/getOneRobot/{robot_name}", response_model=ResponseBaseModel,
                          response_model_exclude_unset=True,
                          summary="根据机器人名称查找机器人，可模糊查询")
async def get_one_robot(robot_name: str):
    """
    根据机器人名称查找机器人
    """
    robot_info = await RobotInfo.filter(robot_name__contains=robot_name, is_del=0) \
        .all() \
        .order_by("-update_robot__update_date") \
        .distinct() \
        .values(
        "robot_id",
        "robot_name",
        "download_counter",
        "publisher_id",
        "category__category_id",
        "category__category_name",
        "details_robot__details_id",
        "details_robot__content",
        "details_robot__cur_version",
        "details_robot__video"
    )
    if not robot_info:
        return ResponseBaseModel(statusCode=ResponseCode.ROBOT_NOT_FOUND_ERROR, msg=ResponseMessage.NoResourceFound)
    tmp = []
    for item in robot_info:
        tmp.append(RobotTotalInfoModel(**item))
    return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, data=tmp, msg=ResponseMessage.Success)


@robot_manager_router.get("/robot/getRobotUpdateInfo/{robot_name}", response_model=ResponseBaseModel,
                          response_model_exclude_unset=True, summary="查询机器人更新信息")
async def get_robot_updateInfo(robot_name: str):
    robotObj = await Curd(RobotInfo).querySingle(is_del=0, robot_name=robot_name)
    if not robotObj:
        return ResponseBaseModel(statusCode=ResponseCode.ROBOT_NOT_FOUND_ERROR, msg=ResponseMessage.NotFondResourceErr)
    robot_updateInfo = await Curd(RobotUpdateInfo).queryAll(is_del=0, robot_id=robotObj.robot_id)
    tmp = []
    for item in robot_updateInfo:
        if item.update_date:
            item.update_date = item.update_date.strftime("%Y-%m-%d %H:%M:%S")
        tmp.append({"robot_id": robotObj.robot_id, "update_id": item.update_id, "update_date": item.update_date,
                    "update_content": item.update_content})
    return ResponseBaseModel(statusCode=ResponseCode.HTTP_200_OK, data=tmp, msg=ResponseMessage.Success)


@robot_manager_router.post("/robot/createOneRobot", dependencies=[Depends(get_current_user)],
                           response_model=ResponseBaseModel, response_model_exclude_unset=True,
                           summary="创建机器人以及相应机器人详情")
async def create_robot(robot: CreateRobotModel):
    """
    创建一个机器人
    """
    c_robot_info = robot.dict()
    # 现根据robot_name查找是否存在相同name的机器人
    robotObj = await Curd(RobotInfo).querySingle(robot_name=c_robot_info.get("robot_name"))
    if not robotObj:
        # 生成一个robot_id
        robot_id = uuid.uuid4()
        await Curd(RobotInfo, RobotDetailsInfo).createRobot(
            RobotInfoModel(**c_robot_info).dict(),
            RobotDetailsInfoModel(**c_robot_info).dict(),
            robot_id=robot_id
        )
        # 返回响应
        return ResponseBaseModel(statusCode=ResponseCode.ROBOT_CREATE_SUCCESS, data=c_robot_info,
                                 msg=ResponseMessage.CreateRobotSuccess)
    return ResponseBaseModel(statusCode=ResponseCode.ROBOT_CREATE_FAILED, msg=ResponseMessage.RobotIsExistErr)


@robot_manager_router.put("/robot/editOneRobot/{robot_name}", dependencies=[Depends(get_current_user)],
                          response_model=ResponseBaseModel, response_model_exclude_unset=True,
                          summary="更新机器人，更新机器人表、详情表、以及增加更新记录")
async def edit_robot(robot_name: str, robot: EditRobotModel):
    """
    更新机器人
    """
    e_robot_info = robot.dict()
    # 根据robot_name查找是否有该机器人
    robotObj = await Curd(RobotInfo).querySingle(robot_name=robot_name, is_del=0)
    if robotObj:
        await Curd(RobotInfo, RobotDetailsInfo, RobotUpdateInfo).editRobot(
            {"robot_id": robotObj.robot_id},
            e_robot_info.get("robot_info"),
            e_robot_info.get("robot_details_info"),
            update_id=uuid.uuid4(),
            update_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            version=e_robot_info.get("robot_details_info").get("cur_version"),
            update_content=e_robot_info.get("robot_update_info").get("update_content"),
            robot_id=robotObj.robot_id
        )

        return ResponseBaseModel(statusCode=ResponseCode.ROBOT_EDIT_SUCCESS,
                                 data={"robot_id": robotObj.robot_id,
                                       "robot_name": robot.dict().get("robot_info").get("robot_name")},
                                 msg=ResponseMessage.EditRobotSuccess)
    else:
        return ResponseBaseModel(statusCode=ResponseCode.ROBOT_EDIT_FAILED, msg=ResponseMessage.EditRobotIsNotExistErr)


@robot_manager_router.delete("/robot/delOneRobot/{robot_name}", dependencies=[Depends(get_current_user)],
                             response_model=ResponseBaseModel, response_model_exclude_unset=True,
                             summary="删除机器人, 以及删除详情、更新记录")
async def del_robot(robot_name: str):
    """
    删除机器人
    """
    # 先查机器人是否存在
    robotObj = await RobotInfo.filter(robot_name=robot_name, is_del=0).first()
    if robotObj:
        await Curd(RobotInfo, RobotDetailsInfo, RobotUpdateInfo).delRobot(robot_id=robotObj.robot_id, is_del=0)
        return ResponseBaseModel(statusCode=ResponseCode.ROBOT_DEL_SUCCESS,
                                 data={"robot_id": robotObj.robot_id, "robot_name": robotObj.robot_name},
                                 msg=ResponseMessage.DelRobotSuccess)
    return ResponseBaseModel(statusCode=ResponseCode.ROBOT_DEL_FAILED,
                             msg=ResponseMessage.DelRobotFailed)
