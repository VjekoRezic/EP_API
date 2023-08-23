from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import WorkCenter
from .serializers import WorkCenterSerializer, WorkCenterDetailSerializer
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly

class WorkCenterViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing WorkCenter objects.

    This ViewSet provides CRUD operations for WorkCenter objects and custom logic for deleting.

    Attributes:
        authentication_classes (tuple): A tuple containing authentication classes used for view authentication.
        permission_classes (list): A list of permission classes for controlling access to the viewset.

    Methods:
        get_serializer_class: Returns the appropriate serializer class based on the action.
        get_queryset: Returns a queryset of WorkCenter objects excluding those marked as deleted.
        destroy: Custom logic to mark a WorkCenter object as deleted.
    """

    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    queryset = WorkCenter.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        """
        Return the serializer class based on the action.

        Returns:
            Serializer: The appropriate serializer class.
        """
        if self.action == 'list' or self.action == 'retrieve':
            return WorkCenterDetailSerializer
        return WorkCenterSerializer

    def get_queryset(self):
        """
        Return a queryset of WorkCenter objects excluding deleted ones.

        Returns:
            QuerySet: A queryset of WorkCenter objects.
        """
        return WorkCenter.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        """
        Mark a WorkCenter object as deleted.

        Overrides the default destroy method to mark the WorkCenter object as deleted instead of hard deletion.

        Returns:
            Response: A response indicating successful deletion.
        """
        instance = self.get_object()

        # Custom delete behavior: Set is_deleted to True
        instance.is_deleted = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
