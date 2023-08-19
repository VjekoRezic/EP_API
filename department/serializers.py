from rest_framework import serializers
from .models import Department
from user.serializers import UserSimpleSerializer



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'is_deleted', 'manager']

class DepartmentDetailSerializer(serializers.ModelSerializer):
    manager = UserSimpleSerializer()  # Include manager details using the ManagerSerializer

    class Meta:
        model = Department
        fields = '__all__'  # Include all fields you need for GET