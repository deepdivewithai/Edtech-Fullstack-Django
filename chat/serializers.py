# serializers.py
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')  # Add sender's username
    receiver_username = serializers.ReadOnlyField(source='receiver.username')  # Add receiver's username

    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'sender_username', 'receiver_username', 'content', 'timestamp')