from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'email', 'city', 'job_title', 'rfid_uid', 'is_deleted', 'workplace', 'workcenter', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Password field is write-only
        }

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']         

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'father_name', 'date_of_birth', 'email', 'city', 'job_title', 'rfid_uid', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user        
    
from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()    