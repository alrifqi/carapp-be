from typing import List, Union
from pydantic import Field, BaseModel
from schema.base import BaseCustomModel, PyObjectId, BaseCustomResponse


class BrandSchema(BaseCustomModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    logo: str
    description: str


class BrandCreateSchema(BaseModel):
    name: str
    logo: str
    description: str


class BrandResponseSchema(BaseCustomResponse):
    data: Union[List[BrandSchema], list, dict]
