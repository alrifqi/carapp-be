import datetime
import pymongo
from typing import List
from bson import ObjectId
from core.database import database
from schema import BrandSchema, BrandCreateSchema
from utils import database_util


brands_collection = database.get_collection("brands")


async def get_brands(page_size: int, page_num: int) -> List[BrandSchema]:
    brands = []
    async for brand in brands_collection.find().skip(database_util.calculate_page_to_skip(page_size, page_num)).limit(page_size).sort("created_at", pymongo.DESCENDING):
        brands.append(brand)
    return brands


async def create_brand(payload: BrandCreateSchema) -> BrandSchema:
    new_brand = await brands_collection.insert_one({ "name": payload.name, "description": payload.description, "logo": payload.logo, "created_at": datetime.datetime.now(), "updated_at": datetime.datetime.now() })
    created_brand = await brands_collection.find_one({"_id": new_brand.inserted_id})
    return created_brand


async def update_brand(id: str, payload: BrandCreateSchema) -> BrandSchema:
    update_brand = await brands_collection.update_one({"_id": id}, {"$set": { "name": payload.name, "description": payload.description, "logo": payload.logo, "updated_at": datetime.datetime.now() }})
    updated_brand = await brands_collection.find_one({"_id": ObjectId(id)})
    return updated_brand


async def remove_brand(id: str) -> None:
    return await brands_collection.delete_one({ "_id": ObjectId(id) })


async def get_brand_by_id(id: str) -> BrandSchema:
    return await brands_collection.find_one({"_id": ObjectId(id)})
