import datetime
import pymongo
from typing import List
from bson import ObjectId
from core.database import database
from schema import CarCreateSchema, CarSchema
from utils import database_util


cars_collection = database.get_collection("cars")


async def create_cars(payload: CarCreateSchema) -> CarSchema:
      new_car = await cars_collection.insert_one({ "name": payload.name, "description": payload.description, "brand_id": payload.brand_id,"created_at": datetime.datetime.now(), "updated_at": datetime.datetime.now() })
      created_brand = await cars_collection.find_one({"_id": new_car.inserted_id})
      return created_brand


async def get_cars(page_size: int, page_num: int) -> List[CarSchema]:
  cars = []
  async for car in cars_collection.find().skip(database_util.calculate_page_to_skip(page_size, page_num)).limit(page_size).sort("created_at", pymongo.DESCENDING):
      cars.append(car)
  return cars


async def get_car_by_id(id: str) -> CarSchema:
    return await cars_collection.find_one({"_id": ObjectId(id)})


async def update_brand(id: str, payload: CarCreateSchema) -> CarSchema:
    update_car = await cars_collection.update_one({"_id": id}, {"$set": { "name": payload.name, "description": payload.description, "brand_id": payload.brand_id, "updated_at": datetime.datetime.now() }})
    update_car = await cars_collection.find_one({"_id": ObjectId(id)})
    return update_car
