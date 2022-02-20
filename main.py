from fastapi import FastAPI
from routers.brands import brands_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


app.include_router(brands_router, tags=["brands"])