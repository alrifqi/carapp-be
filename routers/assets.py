from fastapi import UploadFile, File
from fastapi_utils.inferring_router import InferringRouter

from core.cbv import cbv
from routers._base import BaseApi
from services import assets as assets_service
from schema import CreateAssetsResoponseSchema


assets_router = InferringRouter(prefix="/assets")


@cbv(assets_router)
class BrandsRouter(BaseApi):
    @assets_router.post("", response_model=CreateAssetsResoponseSchema)
    async def post(self, file: UploadFile = File(..., description="A file to be uploaded")):
        data = await assets_service.upload_file(file)
        return self.make_response(data=data)