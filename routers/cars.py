from fastapi_utils.inferring_router import InferringRouter
from fastapi import status, Response

from core.cbv import cbv
from core.exception import NotFoundException
from routers._base import BaseApi
from schema import CarSingleResponseSchema, CarCreateSchema, CreatedCarResponseSchema, CarListResponseSchema, CarResponseSchema
from services import cars as cars_service


car_router = InferringRouter(prefix="/car")


@cbv(car_router)
class BrandsRouter(BaseApi):
    @car_router.get("", response_model=CarListResponseSchema)
    async def get(self, page: int=1, page_size: int = 10):
        data = await cars_service.get_cars(page_size, page)
        return self.make_response(data=data)

    @car_router.post("", response_model=CreatedCarResponseSchema)
    async def post(self, payload: CarCreateSchema, response: Response):
        try:
            data = await cars_service.create_car(payload)
            return self.make_response(data=data)
        except NotFoundException as e:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return self.make_response(message=str(e))

    @car_router.put("/{id}", response_model=CarResponseSchema)
    async def put(self, id: str, payload: CarCreateSchema):
        data = await cars_service.update_car(id, payload)
        return self.make_response(data=data)


    @car_router.get("/{id}", response_model=CarSingleResponseSchema)
    async def get_by_id(self, id: str, response: Response):
        try:
            data = await cars_service.get_car_by_id(id)
            return self.make_response(data=data)
        except NotFoundException as e:
            response.status_code = status.HTTP_404_NOT_FOUND
            return self.make_response(message=str(e))
