from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request

from chat.serializers import ChatSerializer
from chat.models import Chat


@api_view(['GET', 'POST'])
def get_all_chats_api(request: Request):

    if request.method == 'GET':
        query_set = Chat.objects.all()
        ser = ChatSerializer(query_set, many=True)

        return Response({'chats': ser.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        ser = ChatSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)

        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
