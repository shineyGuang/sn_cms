# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 9:47 下午
# @Author  : ShineyZhao
# @File    : main.py
# @Email   : shiney_zhao@163.com
import uvicorn

from app import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='127.0.0.basic',
        port=8000,
        debug=True,
        reload=True,
    )
