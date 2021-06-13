# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 10:43 上午
# @Author  : ShineyZhao
# @File    : main.py
# @Email   : shiney_zhao@163.com
import os.path
import shutil
from pathlib import Path
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from tempfile import NamedTemporaryFile

app = FastAPI()


@app.post("/test/fileUpload", summary="UploadFile方式")
async def test_fileUpload(files: UploadFile = File(...)):
    save_dir = "./uploads"
    try:
        content = await files.read()

        async def writeFile():
            with open(os.path.join(save_dir, "basic.jpg"), "wb") as f:
                f.write(content)

        await writeFile()
        # suffix = Path(files.filename).suffix
        # # 创建一个临时文件并写入
        # with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
        #     shutil.copyfileobj(files.file, tmp)
        #     tmp_file_name = Path(tmp.name).name
    finally:
        files.file.close()

    return {"old_name": files.filename, "tmp_name": os.path.join(save_dir, "basic.jpg")}
