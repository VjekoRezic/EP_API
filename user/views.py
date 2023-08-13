from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
import jwt
import datetime
from django.conf import settings


class UserRegistrationView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                login(request, user)
                token = create_token(user.id)
                resp = Response({"message":"Login successful"}, status=status.HTTP_200_OK)
                resp.set_cookie(key="jwt", value=token, httponly=True, secure=True, samesite="None")
                return resp
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        logout(request)
        resp= Response({"message":"Logout successful"}, status=status.HTTP_200_OK)
        resp.delete_cookie("jwt")
        return resp


def create_token(user_id:int)-> str:
    payload = dict(
        id=user_id,
        exp= datetime.datetime.utcnow() + datetime.timedelta(hours=3) ,
        iat= datetime.datetime.utcnow()
    )
    
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return token