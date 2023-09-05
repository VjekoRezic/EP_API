from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from workorder.consumers import WorkOrderConsumer  # Import your WebSocket consumers here
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'ws/workorder/$', WorkOrderConsumer.as_asgi()),  # Define your WebSocket URL patterns
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
