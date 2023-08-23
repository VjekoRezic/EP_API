from rest_framework import viewsets
from .models import Failure
from .serializers import FailureSerializer, FailureDetailSerializer, FailurePostSerializer
from rest_framework.permissions import IsAuthenticated
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly

class FailureViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Failure objects.

    This ViewSet provides CRUD operations for Failure objects and custom logic for deletion and creation.

    Attributes:
        authentication_classes (tuple): A tuple containing authentication classes used for view authentication.
        permission_classes (list): A list of permission classes for controlling access to the viewset.

    Methods:
        get_serializer_class: Returns the appropriate serializer class based on the action.
        get_queryset: Returns a queryset of Failure objects excluding those marked as deleted.
        perform_destroy: Custom logic to mark a Failure object as deleted.
        perform_create: Custom logic to set the reported_by and work_center fields when creating a Failure.
    """

    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Return the serializer class based on the action.

        Returns:
            Serializer: The appropriate serializer class.
        """
        if self.action in ['retrieve', 'list']:
            return FailureDetailSerializer
        return FailurePostSerializer

    def get_queryset(self):
        """
        Return a queryset of Failure objects excluding deleted ones.

        Returns:
            QuerySet: A queryset of Failure objects.
        """
        return Failure.objects.filter(is_deleted=False)

    def perform_destroy(self, instance):
        """
        Mark a Failure object as deleted.

        Overrides the default perform_destroy method to mark the Failure object as deleted.

        Args:
            instance (Failure): The Failure object to be marked as deleted.
        """
        instance.is_deleted = True
        instance.save()

    def perform_create(self, serializer):
        """
        Set reported_by and work_center fields when creating a Failure.

        Args:
            serializer (FailurePostSerializer): The serializer instance used for creating the Failure object.
        """
        serializer.save(reported_by=self.request.user, work_center=self.request.user.workcenter)
