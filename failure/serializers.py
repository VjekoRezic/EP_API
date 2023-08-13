from rest_framework import serializers
from .models import Failure
from user.serializers import UserSimpleSerializer   

class FailureSerializer(serializers.ModelSerializer):
    reporterted_by = UserSimpleSerializer()
    solved_by = UserSimpleSerializer()
    class Meta:
        model = Failure
        fields = ['id', 'name', 'description', 'reported_by', 'solved_by', 'created_at', 'updated_at', 'is_deleted', 'work_order', 'work_center']