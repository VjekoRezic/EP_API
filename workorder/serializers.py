from rest_framework import serializers
from .models import WO_Category, WO_Status, WorkOrder
from workcenter.serializers import WorkCenterSimpleSerializer
from user.serializers import UserSimpleSerializer
from django.utils import timezone

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

class WorkOrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ['title', 'description', 'due_time', 'work_center', 'category', 'assigned_to', 'status', 'created_by']
        read_only_fields = ['status', 'created_by']

    def create(self, validated_data):
        validated_data["start_time"] = timezone.now()
        validated_data["created_by"] = self.context['request'].user
        validated_data["status"] = WO_Status.objects.get(name="Novi")  # Zamijenite s pravim modelom statusa
        return super().create(validated_data)
    
class WOUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ['title', 'description', 'due_time', 'category', 'assigned_to', 'status']

    def update(self, instance, validated_data):
        # Provjeri i postavi complete_time ako je status "Završeni"
        if 'status' in validated_data and instance.status.name != 'Završeni' and validated_data['status'].name == 'Završeni':
            validated_data['complete_time'] = timezone.now()

        # Ažuriraj updated_at vremenski žig
        validated_data['updated_at'] = timezone.now()

        # Ukloni neposlane polje iz validated_data
        for field in self.fields:
            if field not in self.initial_data:
                validated_data.pop(field, None)

        return super().update(instance, validated_data)