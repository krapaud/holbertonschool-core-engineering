#!/usr/bin/env python3
"""WebSocket server with unicast message delivery."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

CLIENTS = set()


async def connection_handler(websocket):
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        CLIENTS.remove(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
