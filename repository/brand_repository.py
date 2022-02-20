from typing import List

from core.database import database
from schema import BrandSchema, BrandCreateSchema
from utils import database_util


brands_collection = database.get_collection("brands")


async def get_brands(page_size: int, page_num: int) -> List[BrandSchema]:
    brands = []
    async for brand in brands_collection.find().skip(database_util.calculate_page_to_skip(page_size, page_num)).limit(page_size):
        brands.append(brand)
    return brands


async def create_brand(payload: BrandCreateSchema) -> BrandSchema:
    pass