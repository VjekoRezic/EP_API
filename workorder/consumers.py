import json
from channels.generic.websocket import AsyncWebsocketConsumer

class WorkOrderConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for handling work order updates.

    This consumer handles WebSocket connections related to work order updates. It allows clients to connect and receive real-time updates for work orders.

    Attributes:
        channel_name (str): The unique name of the WebSocket channel.
    """

    async def connect(self):
        """
        Handle WebSocket connection.

        This method is called when a WebSocket client establishes a connection. It adds the consumer to the "workorder_updates" group and accepts the connection.
        """
        await self.channel_layer.group_add("workorder_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """
        Handle WebSocket disconnection.

        This method is called when a WebSocket connection is closed. It does not perform any specific action on disconnection.
        
        Args:
            close_code: The code indicating the reason for disconnection.
        """
        pass

    async def update_workorder(self, event):
        """
        Send an update message for a work order.

        This method is called when a work order update event is received. It sends a WebSocket message with the updated work order data.

        Args:
            event (dict): The event data containing the updated work order information.
        """
        message = event["workorder"]
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({"type": "update", "workorder": message}))

    async def create_workorder(self, event):
        """
        Send a create message for a work order.

        This method is called when a new work order is created. It sends a WebSocket message with the newly created work order data.

        Args:
            event (dict): The event data containing the newly created work order information.
        """
        message = event["workorder"]
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({"type": "create", "workorder": message}))

    async def delete_workorder(self, event):
        """
        Send a delete message for a work order.

        This method is called when a work order is deleted. It sends a WebSocket message with the ID of the deleted work order.

        Args:
            event (dict): The event data containing the ID of the deleted work order.
        """
        message = event["workorder_id"]
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({"type": "delete", "workorder_id": message}))
