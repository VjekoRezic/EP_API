from rest_framework import serializers
from .models import Department
from user.serializers import UserSimpleSerializer



class DepartmentSerializer(serializers.ModelSerializer):
    manager = UserSimpleSerializer()  # Use the UserSerializer for the manager field

    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'is_deleted', 'manager']