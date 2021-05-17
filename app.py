from aiohttp import web
import socketio
import user.routes
from config import settings


sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


@sio.on("connect")
async def connect(sid, environ):
    await sio.emit("welcome", "Test socket message!")


def main():
    user.routes.init(app)
    web.run_app(app, host=settings.app.host, port=settings.app.port)
