from typing import List, Optional
from schema import BrandSchema, BrandCreateSchema

from repository import brand_repository


async def get_brands_all(page_size: Optional[int] = 10, page_num: Optional[int] = 1) -> List[BrandSchema]:
    return await brand_repository.get_brands(page_size, page_num)


async def create_brand(payload: BrandCreateSchema) -> BrandSchema:
    pass