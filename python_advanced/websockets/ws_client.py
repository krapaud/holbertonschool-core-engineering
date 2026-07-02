#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio
import websockets


async def connect_and_send(uri="ws://localhost:8765", message="Hello WebSocket"):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


if __name__ == "__main__":
    print(asyncio.run(connect_and_send()))
