from rest_framework import serializers
from .models import WO_Category, WO_Status, WorkOrder

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
