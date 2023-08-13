from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'email', 'city', 'job_title', 'rfid_uid', 'is_deleted', 'workplace', 'workcenter', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},  # Password field is write-only
        }

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']         