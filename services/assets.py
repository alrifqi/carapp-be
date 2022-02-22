import datetime
import os
import shutil

from core.config import settings
from fastapi import UploadFile
from repository import asset_repository

async def upload_file(file: UploadFile):
    file_extension = file.filename.split(".")
    file_extension = file_extension[len(file_extension) - 1]
    saved_filename = f"{int(datetime.datetime.now().timestamp())}.{file_extension}"
    file_path = os.path.join(settings.UPLOAD_PATH, saved_filename)

    with open(file_path, "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)

    return await asset_repository.save_file(saved_filename, file_path)