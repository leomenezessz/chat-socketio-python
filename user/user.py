from db import mongo
from config import settings


async def save(user):
    return await mongo.save(settings.mongo.name, settings.mongo.colletcion, user)
