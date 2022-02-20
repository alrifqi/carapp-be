import fastapi
from typing import List, Union
from fastapi_utils.inferring_router import InferringRouter

from core.cbv import cbv
from routers._base import BaseApi
from schema import BrandSchema, BrandResponseSchema, BrandCreateSchema, BaseErrorValidation
from services import brands as brands_service


brands_router = InferringRouter(prefix="/brand")


@cbv(brands_router)
class BrandsRouter(BaseApi):
    @brands_router.get("", response_model=BrandResponseSchema)
    async def get(self):
        data = await brands_service.get_brands_all()
        return self.make_response(data=data)

    @brands_router.post("", response_model=BrandResponseSchema)
    def post(self, payload: BrandCreateSchema):
        self.make_response(message="brands router")