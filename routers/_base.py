from typing import Union
from fastapi import status


class BaseApi():
    def make_response(self, data=None, message: str = 'success', meta=None):
        if meta is None:
            meta = {}

        if data is None:
            data = {}
        response = {"message": message, "meta": meta, "data": data}
        return response