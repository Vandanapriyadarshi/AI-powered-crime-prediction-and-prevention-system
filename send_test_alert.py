import asyncio
import websockets
import json

async def send_test_alert():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        alert = {"severity": "High", "report": "Armed robbery", "location": "Downtown"}
        await websocket.send(json.dumps(alert))
        print("🚨 Test alert sent!")

asyncio.run(send_test_alert())
