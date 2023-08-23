from rest_framework import serializers
from .models import Workplace

class WorkplaceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Workplace model.

    This serializer defines how a Workplace instance is represented in JSON format.

    Attributes:
        model (Workplace): The model associated with the serializer.
        exclude (list): List of fields to be excluded from serialization.

    Note:
        The 'is_deleted' field is excluded from serialization.

    Example:
        Serialized JSON representation of a Workplace instance:
        {
            "id": 1,
            "name": "Office A",
            "code": "OA",
            "points": "100.00"
        }
    """
    class Meta:
        model = Workplace
        exclude = ['is_deleted']
