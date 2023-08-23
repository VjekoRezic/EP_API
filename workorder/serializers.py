from rest_framework import serializers
from .models import WO_Category, WO_Status, WorkOrder
from workcenter.serializers import WorkCenterSimpleSerializer
from user.serializers import UserSimpleSerializer
from django.utils import timezone

class WO_CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the WO_Category model.

    Attributes:
        model (WO_Category): The WO_Category model class.
        fields (list): The fields to include in the serialized representation.
    """

    class Meta:
        model = WO_Category
        fields = ['id', 'name', 'is_deleted']

class WO_StatusSerializer(serializers.ModelSerializer):
    """
    Serializer for the WO_Status model.

    Attributes:
        model (WO_Status): The WO_Status model class.
        fields (list): The fields to include in the serialized representation.
    """

    class Meta:
        model = WO_Status
        fields = ['id', 'name', 'is_deleted']

class WorkOrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the WorkOrder model.

    Attributes:
        model (WorkOrder): The WorkOrder model class.
        fields (list): The fields to include in the serialized representation.
    """

    class Meta:
        model = WorkOrder
        fields = ['id', 'title', 'description', 'start_time', 'due_time', 'complete_time', 'work_center', 'category', 'created_by', 'assigned_to', 'status', 'created_at', 'updated_at', 'is_deleted']

class WorkOrderDetailSerializer(serializers.ModelSerializer):
    """
    Detail serializer for the WorkOrder model.

    Attributes:
        work_center (CharField): The serialized work center name.
        category (CharField): The serialized category name.
        created_by (CharField): The serialized full name of the creator.
        assigned_to (CharField): The serialized full name of the assignee.
        status (CharField): The serialized display name of the status.
        model (WorkOrder): The WorkOrder model class.
        fields (list): The fields to include in the serialized representation.
    """

    work_center = serializers.CharField(source='work_center.name')
    category = serializers.CharField(source='category.name')
    created_by = serializers.CharField(source='created_by_get_full_name')
    assigned_to = serializers.CharField(source='assigned_to_get_full_name')
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = WorkOrder
        fields = ['id', 'title', 'description', 'start_time', 'due_time', 'complete_time', 'work_center', 'category', 'created_by', 'assigned_to', 'status', 'created_at', 'updated_at', 'is_deleted']

class WorkOrderPostSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new WorkOrder.

    Attributes:
        model (WorkOrder): The WorkOrder model class.
        fields (list): The fields to include in the serialized representation.
        read_only_fields (list): The fields that are read-only.
    """

    class Meta:
        model = WorkOrder
        fields = ['title', 'description', 'due_time', 'work_center', 'category', 'assigned_to', 'status', 'created_by']
        read_only_fields = ['status', 'created_by']

    def create(self, validated_data):
        """
        Create a new WorkOrder instance.

        Args:
            validated_data (dict): The validated data to create the instance.

        Returns:
            WorkOrder: The created WorkOrder instance.
        """
        validated_data["start_time"] = timezone.now()
        validated_data["created_by"] = self.context['request'].user
        validated_data["status"] = WO_Status.objects.get(name="Novi")  # Replace with the actual status model
        return super().create(validated_data)

class WOUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating a WorkOrder.

    Attributes:
        model (WorkOrder): The WorkOrder model class.
        fields (list): The fields to include in the serialized representation.
    """

    class Meta:
        model = WorkOrder
        fields = ['title', 'description', 'due_time', 'category', 'assigned_to', 'status']

    def update(self, instance, validated_data):
        """
        Update a WorkOrder instance.

        Args:
            instance (WorkOrder): The instance to be updated.
            validated_data (dict): The validated data for updating.

        Returns:
            WorkOrder: The updated WorkOrder instance.
        """
        # Check and set complete_time if status is "Završeni" (Completed)
        if 'status' in validated_data and instance.status.name != 'Završeni' and validated_data['status'].name == 'Završeni':
            validated_data['complete_time'] = timezone.now()

        # Update the updated_at timestamp
        validated_data['updated_at'] = timezone.now()

        # Remove unsent field from validated_data
        for field in self.fields:
            if field not in self.initial_data:
                validated_data.pop(field, None)

        return super().update(instance, validated_data)
