from typing import List, Union
from bson import ObjectId
from pydantic import Field, BaseModel
from schema.base import PyObjectId, BaseCustomResponse


class AssetSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    filepath: str
    filename: str

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


class CreateAssetsResoponseSchema(BaseCustomResponse):
    data: AssetSchema
