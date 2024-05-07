from rest_framework import serializers
from chat.models import Chat, ChatQuestion


class ChatTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'title', 'created_at')


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class ChatQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatQuestion
        fields = '__all__'


class ChatDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
