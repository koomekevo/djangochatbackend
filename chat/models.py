from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    # Add any other fields you want for the user

    def __str__(self):
        return self.username

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username}: {self.content}"
