from django.urls import path
from .views import UserListCreateView, MessageListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
]
