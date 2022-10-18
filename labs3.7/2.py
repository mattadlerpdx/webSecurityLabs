# A https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities
# Precede this with a walk through the Developer Tools to find where the web socket messages are sent
# to decode the format of the messages you will need to send
import websockets
import asyncio
import json

site = 'acef1fb61f7d8104c05b42cc00a40042.web-security-academy.net'
 
async def chat():
 websocket_uri = f'wss://{site}/chat'
 async with websockets.connect(websocket_uri) as websocket:
   msg = {'message' : "hello <madler>"}
   json_msg = json.dumps(msg)
   print(f"Sending {json_msg}")
   await websocket.send(json_msg)
   resp = await websocket.recv()
   print(f"Received {resp}")


asyncio.get_event_loop().run_until_complete(chat())
    hello(f'ws://{site}/chat')