#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio
import websockets


async def connect_and_send():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(connect_and_send())
