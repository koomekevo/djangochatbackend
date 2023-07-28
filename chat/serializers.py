from rest_framework import serializers
from .models import User, Message

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = '__all__'  # Include all fields of the User model in the serializer

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.
    """
    class Meta:
        model = Message
        fields = '__all__'  # Include all fields of the Message model in the serializer
