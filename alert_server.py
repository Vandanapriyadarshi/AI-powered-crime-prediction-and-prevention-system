# import asyncio
# import websockets
# import json

# connected_clients = set()

# async def alert_server(websocket, path):
#     connected_clients.add(websocket)
#     try:
#         async for message in websocket:
#             print(f"Received: {message}")
#     except websockets.exceptions.ConnectionClosed:
#         print("Client disconnected")
#     finally:
#         connected_clients.remove(websocket)

# async def send_alert(data):
#     uri = "ws://localhost:6789"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send(json.dumps(data))
   

# async def main():
#     async with websockets.serve(alert_server, "localhost", 6789):
#         print("✅ WebSocket server running at ws://localhost:6789")
#         await asyncio.Future()  # Run forever

# if __name__ == "__main__":
#     import sys
#     if sys.platform.startswith('win'):
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(main())
import asyncio
import websockets
import json

connected_clients = set()

# Broadcast alert to all connected clients
async def broadcast_alert(alert):
    if connected_clients:
        message = json.dumps(alert)
        await asyncio.gather(*[client.send(message) for client in connected_clients])

# WebSocket handler
async def alert_server(websocket, path):
    print("📡 Client connected")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print("📥 Received message:", message)
            alert_data = json.loads(message)
            await broadcast_alert(alert_data)  # Send it to all other clients
    except websockets.exceptions.ConnectionClosed:
        print("❌ Client disconnected")
    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        connected_clients.remove(websocket)




# Start server
async def main():
    print("🚀 Starting WebSocket server...")
    async with websockets.serve(alert_server, "localhost", 6790, ping_interval=None):
        print("✅ WebSocket server running at ws://localhost:6790")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    import sys
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
