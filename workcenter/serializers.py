from rest_framework import serializers
from .models import WorkCenter
from department.serializers import DepartmentDetailSerializer

class WorkCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkCenter
        fields = ['id', 'name', 'description', 'department', 'is_deleted']

class WorkCenterDetailSerializer(serializers.ModelSerializer):
    department = DepartmentDetailSerializer()  # Include department details using the DepartmentDetailSerializer
    class Meta:
        model = WorkCenter
        fields = ['id', 'name', 'description', 'department', 'is_deleted']        