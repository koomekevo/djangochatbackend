from rest_framework import generics
from .models import User, Message
from .serializers import UserSerializer, MessageSerializer

class UserListCreateView(generics.ListCreateAPIView):
    """
    API view to list all users or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    """
    API view to list all messages or create a new message.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
