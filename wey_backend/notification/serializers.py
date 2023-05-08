from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'body', 'type_of_notification', 'post_id', 'created_for_id')