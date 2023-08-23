from rest_framework import serializers
from .models import WO_Category, WO_Status, WorkOrder
from workcenter.serializers import WorkCenterSimpleSerializer
from user.serializers import UserSimpleSerializer

class WO_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WO_Category
        fields = ['id', 'name', 'is_deleted']

class WO_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WO_Status
        fields = ['id', 'name', 'is_deleted']

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ['id', 'title', 'description', 'start_time', 'due_time', 'complete_time', 'work_center', 'category', 'created_by', 'assigned_to', 'status', 'created_at', 'updated_at', 'is_deleted']

class WorkOrderDetailSerializer(serializers.ModelSerializer):
    work_center = serializers.CharField(source='work_center.name')
    category = serializers.CharField(source='category.name')
    created_by = serializers.CharField(source='created_by_get_full_name')
    assigned_to = serializers.CharField(source='assigned_to_get_full_name')
    status = serializers.CharField(source='get_status_display')
    class Meta:
        model = WorkOrder
        fields = ['id', 'title', 'description', 'start_time', 'due_time', 'complete_time', 'work_center', 'category', 'created_by', 'assigned_to', 'status', 'created_at', 'updated_at', 'is_deleted']
