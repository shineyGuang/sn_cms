# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 11:23 上午
# @Author  : ShineyZhao
# @File    : curd.py
# @Email   : shiney_zhao@163.com
from tortoise.transactions import atomic


class Curd(object):
    def __init__(self, model, model2=None, model3=None):
        self.__model__ = model
        self.__model2__ = model2
        self.__model3__ = model3

    @atomic()
    async def queryAll(self, **query):
        return await self.__model__.filter(**query).all()

    @atomic()
    async def querySingle(self, **query):
        return await self.__model__.filter(**query).first()

    @atomic()
    async def create(self, **kwargs):
        return await self.__model__.create(**kwargs)

    @atomic()
    async def update(self, query: dict, **kwargs):
        return await self.__model__.filter(**query).update(**kwargs)

    @atomic()
    async def delete(self, **query):
        await self.__model__.filter(**query).update(is_del=1)

    @atomic()
    async def createRobot(self, robot_info: dict, robot_details: dict, **kwargs):
        await self.__model__.create(**robot_info, **kwargs)
        await self.__model2__.create(**robot_details, **kwargs)

    @atomic()
    async def editRobot(self, robot_id_dict: dict, update_info: dict, update_details: dict, **create_info):
        await self.__model__.filter(**robot_id_dict).update(**update_info)
        await self.__model2__.filter(**robot_id_dict).update(**update_details)
        await self.__model3__.create(**create_info)

    @atomic()
    async def delRobot(self, **query):
        await self.__model__.filter(**query).update(is_del=1)
        await self.__model2__.filter(**query).update(is_del=1)
        await self.__model3__.filter(**query).update(is_del=1)
