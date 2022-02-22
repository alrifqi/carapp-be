from typing import List, Optional
from schema import BrandSchema, BrandCreateSchema

from repository import brand_repository


async def get_brands_all(page_size: Optional[int] = 10, page_num: Optional[int] = 1) -> List[BrandSchema]:
    return await brand_repository.get_brands(page_size, page_num)


async def create_brand(payload: BrandCreateSchema) -> BrandSchema:
    return await brand_repository.create_brand(payload)


async def update_brand(id: str, payload: BrandCreateSchema) -> BrandSchema:
    return await brand_repository.update_brand(id, payload)


async def remove_brand(id: str) -> None:
    return await brand_repository.remove_brand(id)


async def get_brand_by_id(id: str) -> BrandSchema:
    return await brand_repository.get_brand_by_id(id)
