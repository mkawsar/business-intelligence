from .settings import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from ..models.user import User

async def startDB():
    # Client motor client
    client = AsyncIOMotorClient(settings.DB_URL)

    # Init beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[User])
