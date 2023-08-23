from rest_framework import serializers
from .models import Failure
from user.serializers import UserSimpleSerializer   
from workcenter.serializers import WorkCenterSimpleSerializer as Work

class FailureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Failure
        fields = ['id', 'name', 'description', 'reported_by', 'created_at', 'updated_at', 'is_deleted', 'work_order', 'work_center']

class FailureDetailSerializer(serializers.ModelSerializer):
    reported_by = UserSimpleSerializer()
    work_center = Work()
    class Meta:
        model = Failure
        fields = ['id', 'name', 'description', 'reported_by', 'created_at', 'updated_at', 'is_deleted', 'work_order', 'work_center']

class FailurePostSerializer(serializers.ModelSerializer):
    reported_by = serializers.CharField(read_only=True, source='reported_by.username')
    work_center = serializers.CharField(read_only=True, source='work_center.name') 
    class Meta:
        model = Failure
        fields = ['id', 'name', 'description','reported_by', 'updated_at', 'work_order', 'work_center']    
        extra_kwargs = {'reported_by': {'read_only': True}, 'updated_at': {'read_only': True}, 'work_center': {'read_only': True}}
            