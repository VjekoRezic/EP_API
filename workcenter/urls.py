from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkCenterViewSet

router = DefaultRouter()
router.register(r'work-centers', WorkCenterViewSet, basename='work-center')

urlpatterns = [
    path('', include(router.urls)),
]
