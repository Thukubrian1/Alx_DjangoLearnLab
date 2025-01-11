from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(User, related_name='actions', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # e.g., "liked", "commented", "followed"
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)  # ID of the object the notification is related to
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Whether the notification is read or not

    def __str__(self):
        return f"{self.actor.username} {self.verb} {self.target}"

    class Meta:
        ordering = ['-timestamp']
