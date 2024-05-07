from rest_framework import serializers
from chat.models import Chat, ChatQuestion


class ChatTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'title', 'created_at')


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class ChatQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatQuestion
        fields = '__all__'


class ChatDetailsSerializer(serializers.ModelSerializer):
    chat_questions = ChatQuestionSerializer(many=True)

    class Meta:
        model = Chat
        fields = '__all__'


class ChatQuestionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatQuestion
        fields = ('question_type', 'quantity')


class ChatCreateSerializer(serializers.ModelSerializer):
    chat_questions = ChatQuestionWriteSerializer(many=True)

    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        chat_questions_data = validated_data.pop('chat_questions')
        chat = Chat.objects.create(**validated_data)
        for question_data in chat_questions_data:
            ChatQuestion.objects.create(chat=chat, **question_data)
        return chat
