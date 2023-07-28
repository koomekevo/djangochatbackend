from django.urls import path
from .views import UserListCreateView, GroupListCreateView, MessageListCreateView, VoiceCallListCreateView, VideoCallListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('voice-calls/', VoiceCallListCreateView.as_view(), name='voice-call-list-create'),
    path('video-calls/', VideoCallListCreateView.as_view(), name='video-call-list-create'),
]
