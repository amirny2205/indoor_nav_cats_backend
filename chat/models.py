from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class MessageModel(models.Model):
    msg_to = models.ForeignKey(User, related_name='received_message', on_delete=models.CASCADE)
    msg_from = models.ForeignKey(User, related_name='sent_message', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content
