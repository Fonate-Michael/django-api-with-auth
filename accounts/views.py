


from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken



def get_user_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = get_user_token(user)

            return Response({
                'user': {
                    'user_id': user.id,
                    'user_name': user.username
                },
                'token': token
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = get_user_token(user)

            return Response({
                'user': {
                    'user_id': user.id,
                    'username': user.username
                },
                'token': token

            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)