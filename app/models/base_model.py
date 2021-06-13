# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 15:55
# @Author  : 20019236
# @File    : base_model.py
# @Software: fastApi_CLI-master
from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class MyAbstractBaseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)
    is_del = fields.IntField(null=True, default=0)

    class Meta:
        abstract = True


class UserInfo(MyAbstractBaseModel):
    auth_user_id = fields.CharField(255, null=False, unique=True)
    username = fields.CharField(100, null=True)
    is_admin = fields.IntField(default=0)
    password_hash = fields.CharField(255)
    avatar = fields.CharField(100, null=True, default='98d2d0f6-6851-49a8-8d31-8603204cc7311591066453.png')

    robots: fields.ReverseRelation["RobotInfo"]

    class Meta:
        table = "user_info"
        table_description = "用户表"
        ordering = ["created_at", "id"]

    class PydanticMeta:
        exclude = ["created_at", "modified_at", "id"]

    def __str__(self):
        return self.auth_user_id if self.auth_user_id else "UserInfoModel"


class CategoryInfo(MyAbstractBaseModel):
    category_id = fields.CharField(50, null=False, unique=True)
    category_name = fields.CharField(50, unique=True)

    robots: fields.ReverseRelation["RobotInfo"]

    class Meta:
        table = "category_info"
        table_description = "分类表"
        ordering = ["created_at", "id"]

    class PydanticMeta:
        exclude = ["created_at", "modified_at", "id"]

    def __str__(self):
        return self.category_id if self.category_id else "CategoryInfoModel"


# CategoryQueryModel = pydantic_model_creator(CategoryInfo, name="Category")


class RobotInfo(MyAbstractBaseModel):
    robot_id = fields.CharField(255, unique=True)
    robot_name = fields.CharField(255, null=False)
    publisher: fields.ForeignKeyRelation["UserInfo"] = fields.ForeignKeyField(
        "models.UserInfo", related_name="robots", to_field="auth_user_id",
    )
    download_counter = fields.IntField(default=666)
    image = fields.TextField(null=True)
    category: fields.ForeignKeyRelation["CategoryInfo"] = fields.ForeignKeyField(
        "models.CategoryInfo", related_name="robots", to_field="category_id"
    )
    details_robot: fields.ReverseRelation["RobotDetailsInfo"]
    update_robot: fields.ReverseRelation["RobotUpdateInfo"]

    class Meta:
        table = "robot_info"
        table_description = "机器人应用"
        ordering = ["created_at", "id"]

    class PydanticMeta:
        exclude = ["created_at", "modified_at", "id"]

    def __str__(self):
        return self.robot_id if self.robot_id else "RobotInfo"


# RobotQueryModel = pydantic_model_creator(RobotInfo, name="RobotQueryModel")


class RobotDetailsInfo(MyAbstractBaseModel):
    details_id = fields.CharField(255, unique=True)
    content = fields.TextField()
    cur_version = fields.CharField(255, default="v1.0.0")
    video = fields.CharField(255, null=True)
    robot: fields.ForeignKeyRelation["RobotInfo"] = fields.ForeignKeyField(
        "models.RobotInfo", related_name="details_robot", to_field="robot_id"
    )

    class Meta:
        table = "robot_details_info"
        table_description = "机器人详情"
        ordering = ["created_at", "id"]

    class PydanticMeta:
        exclude = ["created_at", "modified_at", "id"]

    def __str__(self):
        return self.details_id if self.details_id else "RobotDetailsInfo"


# RobotDetailsQueryModel = pydantic_model_creator(RobotDetailsInfo, name="RobotDetailsQueryModel")


class RobotUpdateInfo(MyAbstractBaseModel):
    update_id = fields.CharField(255, unique=True)
    robot: fields.ForeignKeyRelation["RobotInfo"] = fields.ForeignKeyField(
        "models.RobotInfo", related_name="update_robot", to_field="robot_id"
    )
    update_date = fields.DatetimeField(auto_now_add=True)
    version = fields.CharField(255, null=True)
    update_content = fields.TextField(null=True)

    class Meta:
        table = "robot_update_info"
        table_description = "机器人更新历史"
        ordering = ["created_at", "id"]

    class PydanticMeta:
        exclude = ["created_at", "modified_at", "id"]

    def __str__(self):
        return self.update_id if self.update_id else "RobotUpdateInfo"

# RobotUpdateQueryModel = pydantic_model_creator(RobotUpdateInfo, name="RobotUpdateQueryModel")
