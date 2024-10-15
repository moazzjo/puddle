from django.db import models
from django.contrib.auth import get_user_model
from item.models import Item

# Create your models here.

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(get_user_model(), related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)


class ConversationMessage(models.Model):
    conversation= models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(get_user_model(), related_name='created_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)