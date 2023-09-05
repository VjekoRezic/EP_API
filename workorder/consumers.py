import json
from channels.generic.websocket import AsyncWebsocketConsumer

class WorkOrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("workorder_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def update_workorder(self, event):
        message = event["workorder"]
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({"type":"update","workorder": message}))

    async def create_workorder(self, event):
        message = event["workorder"]
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({"type":"create","workorder": message}))

    async def delete_workorder(self, event):        
        message = event["workorder_id"]
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({"type":"delete","workorder_id": message}))        