from rest_framework import serializers
from .models import Failure
from user.serializers import UserSimpleSerializer   
from workcenter.serializers import WorkCenterSimpleSerializer as Work

class FailureSerializer(serializers.ModelSerializer):
    """
    Serializer for Failure model.

    Serializes the Failure model to JSON and validates incoming data.

    Attributes:
        None

    Methods:
        None
    """

    class Meta:
        model = Failure
        fields = ['id', 'name', 'description', 'reported_by', 'created_at', 'updated_at', 'is_deleted', 'work_order', 'work_center']

class FailureDetailSerializer(serializers.ModelSerializer):
    """
    Detailed serializer for Failure model.

    Extends FailureSerializer to include user and work center details.

    Attributes:
        None

    Methods:
        None
    """

    reported_by = UserSimpleSerializer()
    work_center = Work()

    class Meta:
        model = Failure
        fields = ['id', 'name', 'description', 'reported_by', 'created_at', 'updated_at', 'is_deleted', 'work_order', 'work_center']

class FailurePostSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a Failure object.

    Includes minimal fields needed for creating a Failure.

    Attributes:
        None

    Methods:
        None
    """

    reported_by = serializers.CharField(read_only=True, source='get_name')
    work_center = serializers.CharField(read_only=True, source='work_center.name') 

    class Meta:
        model = Failure
        fields = ['id', 'name', 'description', 'reported_by', 'updated_at', 'work_order', 'work_center']    
        extra_kwargs = {'reported_by': {'read_only': True}, 'updated_at': {'read_only': True}, 'work_center': {'read_only': True}}
