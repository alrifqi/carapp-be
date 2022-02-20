from motor import motor_asyncio

from core.config import settings

client = motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
database = client.carproduct
