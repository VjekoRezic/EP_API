from rest_framework import serializers
from .models import WorkCenter

class WorkCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkCenter
        fields = ['id', 'name', 'description', 'department', 'is_deleted']