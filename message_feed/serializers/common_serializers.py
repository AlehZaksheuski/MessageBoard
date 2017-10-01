from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from message_feed.models import Message
from message_feed.constants.common import DEFAULT_DATETIME_FORMAT


class MessageSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format=DEFAULT_DATETIME_FORMAT, read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class MessageCommentSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format=DEFAULT_DATETIME_FORMAT, read_only=True)
    children = RecursiveField(required=False, many=True, allow_null=True, source='message_set')

    class Meta:
        model = Message
        fields = ('id', 'depth', 'created_on', 'children', 'has_children', 'text')