from rest_framework import viewsets
from .models import Failure
from .serializers import FailureSerializer, FailureDetailSerializer, FailurePostSerializer
from rest_framework.permissions import IsAuthenticated
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly

class FailureViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return FailureDetailSerializer
        return FailurePostSerializer

    def get_queryset(self):
        return Failure.objects.filter(is_deleted=False)

    def perform_destroy(self, instance):
        # Custom delete behavior: Set is_deleted to True
        instance.is_deleted = True
        instance.save()

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user, work_center=self.request.user.workcenter)