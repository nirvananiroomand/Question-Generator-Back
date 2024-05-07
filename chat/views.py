from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from chat.models import Chat, ChatQuestion
from chat.serializers import ChatTitleSerializer, ChatDetailsSerializer, ChatQuestionSerializer, \
    ChatSerializer


@api_view(['GET', 'POST'])
def chats_api(request: Request):
    if request.method == 'GET':
        # Retrieve all chats
        query_set = Chat.objects.all()
        ser = ChatTitleSerializer(query_set, many=True)
        return Response({'chats': ser.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Create a new chat
        ser = ChatCreateSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)

        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_chat_details_api_deprecated(request: Request, chat_id):
    # Method 1
    chat = Chat.objects.get(id=chat_id)
    chat_questions_qs = ChatQuestion.objects.filter(chat_id=chat_id)
    questions = ChatQuestionSerializer(chat_questions_qs, many=True).data
    ser = ChatSerializer(instance=chat)
    result = ser.data
    result['chat_questions'] = questions
    return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_chat_details_api(request: Request, chat_id):
    # Method 2
    chat = Chat.objects.get(id=chat_id)
    ser = ChatDetailsSerializer(instance=chat)
    return Response(ser.data, status=status.HTTP_200_OK)
