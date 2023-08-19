from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import WorkCenter
from .serializers import WorkCenterSerializer, WorkCenterDetailSerializer
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly


class WorkCenterViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    queryset = WorkCenter.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return WorkCenterDetailSerializer
        return WorkCenterSerializer

    def get_queryset(self):
        # Only include objects where is_deleted is False
        return WorkCenter.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Custom delete behavior: Set is_deleted to True
        instance.is_deleted = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)