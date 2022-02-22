from typing import List, Union, Optional
from bson import ObjectId
from pydantic import Field, BaseModel, validator
from schema.base import PyObjectId, BaseCustomResponse
from .brand_schema import BrandSchema
from services import brands as brands_service
from repository import brand_repository


class CarSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: str
    brand_id: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "string",
                "description": "string",
                "logo": "string",
                "id": "string"
            }
        }


class CarResponseSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: str
    brand_id: str
    brand: BrandSchema

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "string",
                "description": "string",
                "logo": "string",
                "id": "string"
            }
        }


class CarCreateSchema(BaseModel):
    name: str
    logo: str
    description: str
    brand_id: str


class CreatedCarResponseSchema(BaseCustomResponse):
    data: Union[CarResponseSchema, dict]


class CarListResponseSchema(BaseCustomResponse):
    data: Union[List[CarResponseSchema], list, dict]


class CarSingleResponseSchema(BaseCustomResponse):
    data: Union[CarResponseSchema, dict]
