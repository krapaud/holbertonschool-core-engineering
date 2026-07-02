#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio
import os
import sys
import websockets


async def connect_and_send(uri="ws://localhost:8765", message="Hello WebSocket"):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


if __name__ == "__main__":
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    message = os.environ.get("WS_MESSAGE", "Hello WebSocket")
    sys.stdout.write(str(asyncio.run(connect_and_send(uri, message))))
