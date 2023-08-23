from rest_framework import serializers
from .models import WorkCenter
from department.serializers import DepartmentDetailSerializer

class WorkCenterSerializer(serializers.ModelSerializer):
    """
    Serializer for the WorkCenter model.

    Serializes all fields of the WorkCenter model.

    Attributes:
        None
    """

    class Meta:
        model = WorkCenter
        fields = ['id', 'name', 'description', 'department', 'is_deleted']

class WorkCenterDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the WorkCenter model, including department details.

    Serializes all fields of the WorkCenter model and includes department details using DepartmentDetailSerializer.

    Attributes:
        None
    """

    department = DepartmentDetailSerializer()  # Include department details using the DepartmentDetailSerializer

    class Meta:
        model = WorkCenter
        fields = ['id', 'name', 'description', 'department', 'is_deleted']        

class WorkCenterSimpleSerializer(serializers.ModelSerializer):
    """
    Serializer for a simplified representation of the WorkCenter model.

    Serializes a simplified version of the WorkCenter model with fewer fields.

    Attributes:
        None
    """

    class Meta:
        model = WorkCenter
        fields = ['id', 'name']
