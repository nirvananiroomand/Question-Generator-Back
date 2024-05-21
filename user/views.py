from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import SignupSerializer


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request, *args, **kwargs):
    ser = SignupSerializer(data=request.data)
    if ser.is_valid():
        user = ser.save()
        tokens = RefreshToken.for_user(user)
        response = ser.data
        response['tokens'] = {
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
