#!/usr/bin/env python3
"""WebSocket server with broadcast message delivery."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

CLIENTS = set()


async def broadcast(message):
    for client in set(CLIENTS):
        try:
            await client.send(f"B:{message}")
        except ConnectionClosed:
            CLIENTS.discard(client)


async def connection_handler(websocket):
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        CLIENTS.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
