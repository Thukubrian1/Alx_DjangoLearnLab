from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from rest_framework.permissions import IsAuthenticated

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications_data = [{"actor": notification.actor.username, "verb": notification.verb, "timestamp": notification.timestamp} for notification in notifications]

        # Mark notifications as read
        notifications.update(read=True)

        return Response(notifications_data, status=status.HTTP_200_OK)
