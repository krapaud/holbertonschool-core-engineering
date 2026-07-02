#!/usr/bin/env python3
"""ASGI application serving an HTML page and a WebSocket echo endpoint."""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse, FileResponse
from starlette.routing import Route, WebSocketRoute
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


async def homepage(request):
    path = os.path.join(BASE_DIR, "index.html")
    with open(path) as f:
        return HTMLResponse(f.read())


async def chat_js(request):
    path = os.path.join(BASE_DIR, "chat.js")
    return FileResponse(path, media_type="application/javascript")


async def style_css(request):
    path = os.path.join(BASE_DIR, "styles.css")
    return FileResponse(path, media_type="text/css")


async def websocket_endpoint(websocket):
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)


routes = [
    Route("/", homepage),
    Route("/chat.js", chat_js),
    Route("/styles.css", style_css),
    WebSocketRoute("/ws", websocket_endpoint),
]

app = Starlette(routes=routes)
