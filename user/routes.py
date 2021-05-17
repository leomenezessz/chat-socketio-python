from aiohttp import web
from middleware.decorator import response
from user import user


@response
async def register(request):
    new_user = await request.json()
    return await user.save(new_user)


def init(app):
    app.add_routes([web.post("/register", register)])
