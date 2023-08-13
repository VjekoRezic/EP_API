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


    def get_queryset(self):
        # Only include objects where is_deleted is False
        return Department.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        
        return response.Response(status=status.HTTP_204_NO_CONTENT)

