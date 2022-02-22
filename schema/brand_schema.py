from typing import List, Union
from bson import ObjectId
from pydantic import Field, BaseModel, BaseConfig
from schema.base import BaseCustomModel, PyObjectId, BaseCustomResponse


class BrandSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    logo: str
    description: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "string",
                "description": "string",
                "logo": "string"
            }
        }


class BrandCreateSchema(BaseModel):
    name: str
    logo: str
    description: str


class BrandResponseSchema(BaseCustomResponse):
    data: Union[List[BrandSchema], list, dict]


class CreatedBrandResponseSchema(BaseCustomResponse):
    data: BrandSchema
