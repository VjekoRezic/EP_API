from rest_framework import serializers
from .models import Workplace

class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ['id', 'name', 'code', 'points', 'is_deleted']