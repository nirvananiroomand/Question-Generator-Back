from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ai_engine.open_ai import generate_questions
from chat.models import Chat, ChatQuestion
from chat.serializers import ChatTitleSerializer, ChatDetailsSerializer, ChatQuestionSerializer, \
    ChatSerializer, ChatCreateSerializer


@api_view(['GET', 'POST'])
def chats_api(request: Request):
    if request.method == 'GET':
        # Retrieve all chats
        query_set = Chat.objects.filter(user=request.user).order_by('-created_at')
        ser = ChatTitleSerializer(query_set, many=True)
        return Response({'chats': ser.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Create a new chat
        ser = ChatCreateSerializer(data=request.data)
        if ser.is_valid():
            generated_response = generate_questions(content=ser.validated_data['content'], difficulty=ser.validated_data['difficulty'], types_of_questions=ser.validated_data['chat_questions'])
            chat = ser.save()
            chat.response = generated_response
            chat.save()
            result = ser.data
            result['response'] = chat.response
            return Response(result, status=status.HTTP_201_CREATED)

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
    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ser = ChatDetailsSerializer(instance=chat)
    return Response(ser.data, status=status.HTTP_200_OK)
