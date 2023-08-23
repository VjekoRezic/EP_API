from rest_framework import serializers
from .models import Department
from user.serializers import UserSimpleSerializer

class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Department model.

    Serializes the Department model to JSON and validates incoming data.

    Attributes:
        None

    Methods:
        None
    """

    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'is_deleted', 'manager']
        
class DepartmentDetailSerializer(serializers.ModelSerializer):
    """
    Detailed serializer for Department model.

    Extends DepartmentSerializer to include manager details.

    Attributes:
        None

    Methods:
        None
    """

    manager = UserSimpleSerializer()  # Include manager details using the ManagerSerializer

    class Meta:
        model = Department
        fields = '__all__'  # Include all fields you need for GET
