from rest_framework import serializers
from .models import User
from workplace.serializers import WorkplaceSerializer
from workcenter.models import WorkCenter

class WorkCenterSimpleSerializer(serializers.ModelSerializer):
    """
    Serializer for WorkCenter model, providing minimal information.

    Attributes:
        None

    Methods:
        None
    """

    class Meta:
        model = WorkCenter
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.

    Serializes the User model to JSON and validates incoming data.

    Attributes:
        None

    Methods:
        None
    """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'email', 'city', 'job_title', 'rfid_uid', 'is_deleted', 'workplace', 'workcenter', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Password field is write-only
        }

class UserSimpleSerializer(serializers.ModelSerializer):
    """
    Serializer for User model, providing minimal information.

    Attributes:
        None

    Methods:
        None
    """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser']

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Handles user registration and creates a user instance.

    Attributes:
        None

    Methods:
        create: Creates a user instance.
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'father_name', 'date_of_birth', 'email', 'city', 'job_title', 'rfid_uid', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user        
    
class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.

    Attributes:
        email (EmailField): The email address of the user.
        password (CharField): The user's password.
    """

    email = serializers.EmailField()
    password = serializers.CharField()    

class UserRfidLoginSerializer(serializers.Serializer):
    """
    Serializer for user login using RFID UID.

    Attributes:
        rfid_uid (CharField): The RFID UID of the user's card.
    """

    rfid_uid = serializers.CharField()

class UserGetSerializer(serializers.ModelSerializer):
    """
    Detailed serializer for User model.

    Extends UserSerializer to include related workplace and work center details.

    Attributes:
        None

    Methods:
        None
    """

    workplace = WorkplaceSerializer()
    workcenter = WorkCenterSimpleSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'email', 'city', 'job_title', 'rfid_uid', 'workplace', 'workcenter', 'is_staff', 'is_superuser']
