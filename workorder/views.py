from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import WO_Status, WO_Category, WorkOrder
from .serializers import WO_StatusSerializer, WO_CategorySerializer, WorkOrderSerializer, WorkOrderDetailSerializer, WorkOrderPostSerializer, WOUpdateSerializer
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly
from django.utils import timezone

class WO_StatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = WO_StatusSerializer

    def get_queryset(self):
        # Only include objects where is_deleted is False
        return WO_Status.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Custom delete behavior: Set is_deleted to True
        instance.is_deleted = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class WO_CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    queryset = WO_Category.objects.all()
    serializer_class = WO_CategorySerializer

    def get_queryset(self):
        # Only include objects where is_deleted is False
        return WO_Category.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Custom delete behavior: Set is_deleted to True
        instance.is_deleted = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class WorkOrderViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return WorkOrderPostSerializer
        elif self.action == 'update':
            return WOUpdateSerializer
        return WorkOrderDetailSerializer

    def create(self, request, *args, **kwargs):

        request_data = request.data
        request_data['created_by'] = request.user.id
        request_data['status'] = WO_Status.objects.get(name="Novi").id

        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        respSerializer = WorkOrderDetailSerializer(serializer.instance)

        return Response(respSerializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        # Only include objects where is_deleted is False
        return WorkOrder.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Custom delete behavior: Set is_deleted to True
        instance.is_deleted = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    def perform_update(self, serializer):
        instance = serializer.instance

        if "status" in self.request.data and instance.status.name == "Završeni":
            self.request.data["complete_time"] = timezone.now()

        self.request.data["updated_at"] = timezone.now()

        serializer.save()