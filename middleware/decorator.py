from functools import wraps
from aiohttp import web


def response(func):
    @wraps(func)
    async def wrapper(request):
        try:
            result = await func(request)
        except Exception as e:
            return web.Response(status=400, body={"error": e.__repr__()})
        else:
            return web.Response(status=200)

    return wrapper
