from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import SignupSerializer, LoginSerializer
from user.models import CustomUser


# Create your views here.
def obtain_tokens(user):
    tokens = RefreshToken.for_user(user)
    return {
        'refresh': str(tokens),
        'access': str(tokens.access_token),
    }


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request, *args, **kwargs):
    ser = SignupSerializer(data=request.data)
    if ser.is_valid():
        user = ser.save()
        user.last_login = timezone.now()
        user.save()
        response = ser.data
        response['tokens'] = obtain_tokens(user)
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request, *args, **kwargs):
    ser = LoginSerializer(data=request.data)
    if ser.is_valid():
        response = ser.data
        user = CustomUser.objects.get(id=ser.validated_data.get("id"))
        user.last_login = timezone.now()
        user.save()
        response['tokens'] = obtain_tokens(user)
        return Response(response, status=status.HTTP_200_OK)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
