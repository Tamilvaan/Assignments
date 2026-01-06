import asyncio
import websockets

connected_users = {}

async def chat_handler(websocket):
    username = None
    try:
        username = await websocket.recv()

        if username in connected_users:
            await websocket.send("❌ Username already in use")
            await websocket.close()
            return

        connected_users[username] = websocket
        print(f"[JOIN] {username} | Active users: {list(connected_users.keys())}")

        await broadcast(f"🔵 {username} joined the chat")

        async for message in websocket:
            print(f"[RECEIVED] From {username}: {message}")
            await broadcast(f"{username}: {message}")

    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        if username and username in connected_users:
            connected_users.pop(username, None)
            print(f"[LEAVE] {username} | Active users: {list(connected_users.keys())}")
            await broadcast(f"🔴 {username} left the chat")

async def broadcast(message):
    print(f"[BROADCAST] {message} → {len(connected_users)} users")
    await asyncio.gather(
        *[ws.send(message) for ws in connected_users.values()],
        return_exceptions=True
    )

async def main():
    async with websockets.serve(chat_handler, "localhost", 8765):
        print("Chat server running on ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())