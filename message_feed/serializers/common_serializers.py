from rest_framework import serializers
from message_feed.models import Message
from rest_framework_recursive.fields import RecursiveField


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('text', 'depth', 'parent')


class MessageCommentSerializer(serializers.ModelSerializer):
    children = RecursiveField(required=False, many=True, allow_null=True, source='message_set')

    class Meta:
        model = Message
        fields = ('id', 'depth', 'created_on', 'updated_on', 'children', 'has_children', 'text')