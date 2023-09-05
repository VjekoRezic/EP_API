from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import WO_Status, WO_Category, WorkOrder
from .serializers import WO_StatusSerializer, WO_CategorySerializer, WorkOrderSerializer, WorkOrderDetailSerializer, WorkOrderPostSerializer, WOUpdateSerializer
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class WO_StatusViewSet(viewsets.ModelViewSet):
    """
    Viewset for WO_Status model.

    Attributes:
        authentication_classes (tuple): The authentication classes.
        permission_classes (list): The permission classes.
        serializer_class (WO_StatusSerializer): The serializer class.
    """
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = WO_StatusSerializer

    def get_queryset(self):
        """
        Get queryset of WO_Status instances.

        Returns:
            queryset: Filtered queryset of WO_Status instances.
        """
        return WO_Status.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        """
        Custom destroy behavior for WO_Status instances.

        Args:
            request: The request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: Response with status.
        """
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WO_CategoryViewSet(viewsets.ModelViewSet):
    """
    Viewset for WO_Category model.

    Attributes:
        authentication_classes (tuple): The authentication classes.
        permission_classes (list): The permission classes.
        queryset (QuerySet): The queryset of all WO_Category instances.
        serializer_class (WO_CategorySerializer): The serializer class.
    """
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    queryset = WO_Category.objects.all()
    serializer_class = WO_CategorySerializer

    def get_queryset(self):
        """
        Get queryset of WO_Category instances.

        Returns:
            queryset: Filtered queryset of WO_Category instances.
        """
        return WO_Category.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        """
        Custom destroy behavior for WO_Category instances.

        Args:
            request: The request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: Response with status.
        """
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WorkOrderViewSet(viewsets.ModelViewSet):
    """
    Viewset for WorkOrder model.

    Attributes:
        authentication_classes (tuple): The authentication classes.
        permission_classes (list): The permission classes.
    """
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Get appropriate serializer class based on action.

        Returns:
            serializer_class: The selected serializer class.
        """
        if self.action == 'create':
            return WorkOrderPostSerializer
        elif self.action == 'update':
            return WOUpdateSerializer
        return WorkOrderDetailSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new WorkOrder instance.

        Args:
            request: The request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: Response with serialized data.
        """
        request_data = request.data
        request_data['created_by'] = request.user.id
        request_data['status'] = WO_Status.objects.get(name="Novi").id
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        respSerializer = WorkOrderDetailSerializer(serializer.instance)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "workorder_updates",
            {
                "type": "create.workorder",
                "workorder":respSerializer.data
            }
        )
        return Response(respSerializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """
        Get queryset of WorkOrder instances.

        Returns:
            queryset: Filtered queryset of WorkOrder instances.
        """
        return WorkOrder.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        """
        Custom destroy behavior for WorkOrder instances.

        Args:
            request: The request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: Response with status.
        """
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "workorder_updates",
            {
                "type": "delete.workorder",
                "workorder_id":instance.id
            }
        )

        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    def perform_update(self, serializer):
        """
        Perform custom update behavior for WorkOrder instances.

        Args:
            serializer: The serializer instance.

        Returns:
            None
        """
        instance = serializer.instance
        if "status" in self.request.data and instance.status.name == "Završeni":
            self.request.data["complete_time"] = timezone.now()
        self.request.data["updated_at"] = timezone.now()
        serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "workorder_updates",
            {
                "type": "update.workorder",
                "workorder":serializer.data
            }
        )
