# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 10:30 下午
# @Author  : ShineyZhao
# @File    : database.py
# @Email   : shiney_zhao@163.com
# mysql数据库url
from tortoise.contrib.fastapi import register_tortoise

from config import configs

SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}".format(
    configs.MYSQL_USER,
    configs.MYSQL_PASSWORD,
    configs.MYSQL_SERVER,
    configs.MYSQL_PORT,
    configs.MYSQL_DB_NAME
)

# 数据库迁移配置
TORTOISE_ORM = {
    "connections": {"default": SQLALCHEMY_DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "app.models.base_model"
            ],
            # 须添加“aerich.models” 后者“models”是上述models.py文件的路径
            "default_connection": "default",
        },
    },
}


def db_init(app):
    register_tortoise(
        app,
        db_url=SQLALCHEMY_DATABASE_URL,
        modules={"models": ["app.models.base_model"]},
        # generate_schemas=True,
        add_exception_handlers=True,
    )
