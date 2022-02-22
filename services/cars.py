from schema import CarCreateSchema
from repository import brand_repository, car_repository
from core.exception import NotFoundException


async def create_car(payload: CarCreateSchema):
    brand = await brand_repository.get_brand_by_id(payload.brand_id)
    if brand is None:
        raise NotFoundException("Invalid Brand ID")

    resp = await car_repository.create_cars(payload)
    resp["brand"] = brand
    return


async def get_cars(page_size: int, page_num: int):
    resps = await car_repository.get_cars(page_size, page_num)
    for resp in resps:
      resp["brand"] = await brand_repository.get_brand_by_id(resp["brand_id"])
    
    return resps


async def get_car_by_id(id: str):
    resp = await car_repository.get_car_by_id(id)
    if resp is None:
        raise NotFoundException("Car By ID Not Found")

    resp["brand"] = await brand_repository.get_brand_by_id(resp["brand_id"])
    return resp


async def update_car(id: str, payload: CarCreateSchema):
    resp = await car_repository.update_brand(id, payload)
    resp["brand"] = await brand_repository.get_brand_by_id(resp["brand_id"])
    return resp
