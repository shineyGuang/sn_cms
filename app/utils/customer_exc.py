#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 19:20
# @Author  : 20019236
# @File    : customer_exc.py
# @Software: webCli-fastApi
"""

自定义异常

"""


class PostParamsError(Exception):
    def __init__(self, err_desc: str = "POST请求参数错误"):
        self.err_desc = err_desc


class TokenAuthError(Exception):
    def __init__(self, err_desc: str = "token认证失败"):
        self.err_desc = err_desc
