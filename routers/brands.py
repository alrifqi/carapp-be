from fastapi_utils.inferring_router import InferringRouter

from core.cbv import cbv
from routers._base import BaseApi
from schema import BrandResponseSchema, BrandCreateSchema, CreatedBrandResponseSchema
from services import brands as brands_service


brands_router = InferringRouter(prefix="/brand")


@cbv(brands_router)
class BrandsRouter(BaseApi):
    @brands_router.get("", response_model=BrandResponseSchema)
    async def get(self, page: int=1, page_size: int = 10):
        data = await brands_service.get_brands_all(page_size, page)
        return self.make_response(data=data)

    @brands_router.post("", response_model=CreatedBrandResponseSchema)
    async def post(self, payload: BrandCreateSchema):
        data = await brands_service.create_brand(payload)
        resp = self.make_response(data=data)
        return resp

    @brands_router.put("/{id}", response_model=CreatedBrandResponseSchema)
    async def put(self, id: str, payload: BrandCreateSchema):
        data = await brands_service.update_brand(id, payload)
        return self.make_response(data=data)


    @brands_router.delete("/{id}")
    async def delete(self, id: str):
        data = await brands_service.remove_brand(id)
        return self.make_response()
