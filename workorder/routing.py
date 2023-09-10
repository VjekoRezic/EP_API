"""
WebSocket Routing Configuration

This module configures WebSocket routing for Django Channels. It defines the WebSocket URL patterns and middleware stack for handling WebSocket connections.

"""

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from workorder.consumers import WorkOrderConsumer  # Import your WebSocket consumers here
from django.urls import re_path

# Define WebSocket URL patterns for routing WebSocket requests to consumers
websocket_urlpatterns = [
    re_path(r'ws/workorder/$', WorkOrderConsumer.as_asgi()),  # Define your WebSocket URL patterns
]

# Configure the ProtocolTypeRouter for handling WebSocket connections
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
