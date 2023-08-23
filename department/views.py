from django.shortcuts import render

from rest_framework import viewsets, response, status
from .models import Department
from .serializers import DepartmentSerializer, DepartmentDetailSerializer
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Department objects.

    This ViewSet provides CRUD operations for Department objects and custom logic for deleting.

    Attributes:
        authentication_classes (tuple): A tuple containing authentication classes used for view authentication.
        permission_classes (list): A list of permission classes for controlling access to the viewset.

    Methods:
        get_serializer_class: Returns the appropriate serializer class based on the action.
        get_queryset: Returns a queryset of Department objects excluding those marked as deleted.
        destroy: Custom logic to mark a Department object as deleted.
    """

    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        """
        Return the serializer class based on the action.

        Returns:
            Serializer: The appropriate serializer class.
        """
        if self.action in ['retrieve', 'list']:
            return DepartmentDetailSerializer
        return DepartmentSerializer

    def get_queryset(self):
        """
        Return a queryset of Department objects excluding deleted ones.

        Returns:
            QuerySet: A queryset of Department objects.
        """
        return Department.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        """
        Mark a Department object as deleted.

        Overrides the default destroy method to mark the Department object as deleted instead of hard deletion.

        Returns:
            Response: A response indicating successful deletion.
        """
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()

        return response.Response(status=status.HTTP_204_NO_CONTENT)
