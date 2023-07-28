from rest_framework import generics
from .models import User, Group, Message, VoiceCall, VideoCall
from .serializers import UserSerializer, GroupSerializer, MessageSerializer, VoiceCallSerializer, VideoCallSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class VoiceCallListCreateView(generics.ListCreateAPIView):
    queryset = VoiceCall.objects.all()
    serializer_class = VoiceCallSerializer

class VideoCallListCreateView(generics.ListCreateAPIView):
    queryset = VideoCall.objects.all()
    serializer_class = VideoCallSerializer
