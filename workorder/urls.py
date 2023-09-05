from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WO_StatusViewSet, WO_CategoryViewSet, WorkOrderViewSet

router = DefaultRouter()
router.register(r'wo-status', WO_StatusViewSet, basename='wo-status')
router.register(r'wo-categories', WO_CategoryViewSet, basename='wo-categories')
router.register(r'work-orders', WorkOrderViewSet, basename='work-orders')

urlpatterns = [
    path('', include(router.urls)),
]

