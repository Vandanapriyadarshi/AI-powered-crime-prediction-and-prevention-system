# import asyncio
# import websockets
# import json

# async def test_alert():
#     uri = "ws://localhost:6789"

#     sample_alerts = [
#         {
#             "crime_type": "Robbery",
#             "location": "Downtown",
#             "severity": "High",
#             "timestamp": "2025-04-06T12:00:00Z"
#         },
#         {
#             "crime_type": "Assault",
#             "location": "Central Park",
#             "severity": "Medium",
#             "timestamp": "2025-04-06T12:05:00Z"
#         },
#         {
#             "crime_type": "Theft",
#             "location": "Mall Street",
#             "severity": "Low",
#             "timestamp": "2025-04-06T12:10:00Z"
#         },
#         {
#             "crime_type": "Burglary",
#             "location": "5th Avenue",
#             "severity": "High",
#             "timestamp": "2025-04-06T12:15:00Z"
#         }
#     ]

#     try:
#         async with websockets.connect(uri) as websocket:
#             for alert in sample_alerts:
#                 await websocket.send(json.dumps(alert))
#                 print(f"✅ Sent alert: {alert['crime_type']}")
#                 await asyncio.sleep(1)
#     except Exception as e:
#         print("❌ Failed to send alerts:", e)

# if __name__ == "__main__":
#     asyncio.run(test_alert())


import asyncio
import websockets
import json

async def test_alert():
    uri = "ws://localhost:6789"  # Ensure this matches the server port
    data = {
        "crime_type": "Robbery",
        "location": "Downtown",
        "severity": "High",
        "timestamp": "2025-04-06T12:00:00Z",
        "description": "Armed robbery reported at Downtown bank."
    }

    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(data))
            print(f"✅ Sent alert: {data['crime_type']}")
    except Exception as e:
        print(f"❌ Failed to send alerts: {e}")


if __name__ == "__main__":
    asyncio.run(test_alert())
