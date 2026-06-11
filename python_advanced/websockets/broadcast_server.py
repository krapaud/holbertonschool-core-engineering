#!/usr/bin/env python3
"""WebSocket server with broadcast message delivery."""
import asyncio
import websockets

CLIENTS = set()


async def broadcast(message):
    for client in set(CLIENTS):
        try:
            await client.send(f"B:{message}")
        except websockets.exceptions.ConnectionClosed:
            CLIENTS.discard(client)


async def handler(websocket):
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message)
    finally:
        CLIENTS.discard(websocket)


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
