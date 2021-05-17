
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient

_client = AsyncIOMotorClient(settings.mongo.url)


async def find(db_name, coll_name, query):
    db = _client[db_name]
    coll = db[coll_name]
    return await coll.find(query)


async def save(db_name, coll_name, doc):
    db = _client[db_name]
    coll = db[coll_name]
    return await coll.insert_one(doc)
