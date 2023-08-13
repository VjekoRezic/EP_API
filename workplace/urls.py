from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkplaceViewSet

router = DefaultRouter()
router.register(r'workplaces', WorkplaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]