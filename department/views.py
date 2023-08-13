from django.shortcuts import render

from rest_framework import viewsets, response, status
from .models import Department
from .serializers import DepartmentSerializer
from user.authentication import CustomUserAuth
from user.permissions import IsAdminOrReadOnly

class DepartmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.is_deleted:
            return response.Response({"detail": "This department is already deleted."}, status=status.HTTP_400_BAD_REQUEST)
        
        instance.is_deleted = True
        instance.save()
        
        return response.Response(status=status.HTTP_204_NO_CONTENT)
