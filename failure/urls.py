from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FailureViewSet

router = DefaultRouter()
router.register(r'failures', FailureViewSet, basename='failure')

urlpatterns = [
    path('', include(router.urls)),
]