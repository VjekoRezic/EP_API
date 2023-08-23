from rest_framework import viewsets
from .models import Workplace
from .serializers import WorkplaceSerializer
from user.permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from user.authentication import CustomUserAuth

class WorkplaceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Workplace objects.

    This ViewSet provides CRUD operations for Workplace objects and custom logic for deleting.

    Attributes:
        authentication_classes (tuple): A tuple containing authentication classes used for view authentication.
        permission_classes (list): A list of permission classes for controlling access to the viewset.

    Methods:
        get_queryset: Returns a queryset of Workplace objects excluding those marked as deleted.
        destroy: Custom logic to mark a Workplace object as deleted.
    """

    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    queryset = Workplace.objects.filter(is_deleted=False)
    serializer_class = WorkplaceSerializer
    
    def get_queryset(self):
        """
        Return a queryset of Workplace objects excluding deleted ones.

        Returns:
            QuerySet: A queryset of Workplace objects.
        """
        return Workplace.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        """
        Mark a Workplace object as deleted.

        Overrides the default destroy method to mark the Workplace object as deleted instead of hard deletion.

        Returns:
            Response: A response indicating successful deletion.
        """
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
