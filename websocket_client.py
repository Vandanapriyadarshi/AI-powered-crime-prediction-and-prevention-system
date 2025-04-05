import asyncio
import websockets
import json

async def send_alerts(data):
    uri = "ws://localhost:6789"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(data))
            print("🚨 Sent alert to WebSocket server")
    except Exception as e:
        print(f"⚠️ Failed to send WebSocket alert: {e}")
