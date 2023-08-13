from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WO_StatusViewSet

router = DefaultRouter()
router.register(r'wo-status', WO_StatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]