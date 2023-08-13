from rest_framework import viewsets
from .models import Failure
from .serializers import FailureSerializer
from rest_framework.permissions import IsAuthenticated
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly

class FailureViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuth,)
    serializer_class = FailureSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        # Only include objects where is_deleted is False
        return Failure.objects.filter(is_deleted=False)

    def perform_destroy(self, instance):
        # Custom delete behavior: Set is_deleted to True
        instance.is_deleted = True
        instance.save()