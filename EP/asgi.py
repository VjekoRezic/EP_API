"""
ASGI config for EP project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.urls import path, re_path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from workorder.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EP.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

"""
ASGI Application Configuration

This module configures the ASGI (Asynchronous Server Gateway Interface) application for handling both HTTP and WebSocket connections.

Attributes:
    http (ASGI application): The ASGI application for handling HTTP requests.
    websocket (ASGI application): The ASGI application for handling WebSocket connections.
"""
