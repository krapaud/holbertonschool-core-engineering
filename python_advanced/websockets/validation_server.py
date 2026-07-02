#!/usr/bin/env python3
"""WebSocket server with message validation."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    try:
        async for message in websocket:
            stripped = message.strip()
            if stripped == "":
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{stripped}")
    except ConnectionClosed:
        pass


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
