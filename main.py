from fastapi import FastAPI
from  fastapi.staticfiles import StaticFiles

from core.config import settings
from routers.brands import brands_router
from routers.assets import assets_router
from routers.cars import car_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


app.include_router(brands_router, tags=["brands"])
app.include_router(assets_router, tags=["assets"])
app.include_router(car_router, tags=["cars"])
app.mount("/static/assets", StaticFiles(directory=settings.UPLOAD_PATH), name="static-assets")
