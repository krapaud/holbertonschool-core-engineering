#!/usr/bin/env python3
"""WebSocket server with message validation."""
import asyncio
import websockets


async def handler(websocket):
    async for message in websocket:
        stripped = message.strip()
        if stripped == "":
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{stripped}")


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
