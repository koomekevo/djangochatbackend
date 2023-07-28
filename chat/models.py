from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Add any additional fields you want for the user model (e.g., profile picture, etc.)
    pass

    # Add the related_name arguments to prevent clashes with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    # Add a default value for the 'password' field
    password = models.CharField(max_length=128, default='')


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class VoiceCall(models.Model):
    caller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='outgoing_calls')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='incoming_calls')
    timestamp = models.DateTimeField(auto_now_add=True)


class VideoCall(models.Model):
    caller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='outgoing_video_calls')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='incoming_video_calls')
    timestamp = models.DateTimeField(auto_now_add=True)
