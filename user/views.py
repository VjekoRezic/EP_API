from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer, UserSimpleSerializer, UserRfidLoginSerializer
import jwt
import datetime
from django.conf import settings
from .models import User
from .authentication import CustomUserAuth
from department.models import Department
from workcenter.models import WorkCenter
from django.db.models import Q


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

                user_serializer = UserSimpleSerializer(user)

                resp_data = {
                    "message":"Login successful",
                    "user": user_serializer.data
                }    

                resp = Response(resp_data, status=status.HTTP_200_OK)
                resp.set_cookie(key="jwt", value=token, httponly=True, secure=True, samesite="None")
                return resp
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRfidLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRfidLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(rfid_uid=serializer.validated_data['rfid_uid']).first()
            if user:
                login(request, user)
                token = create_token(user.id)

                user_serializer = UserSimpleSerializer(user)

                resp_data = {
                    "message":"Login successful",
                    "user": user_serializer.data
                }    

                resp = Response(resp_data, status=status.HTTP_200_OK)
                resp.set_cookie(key="jwt", value=token, httponly=True, secure=True, samesite="None")
                return resp
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        logout(request)
        resp= Response({"message":"Logout successful"}, status=status.HTTP_200_OK)
        resp.delete_cookie("jwt")
        return resp


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomUserAuth,]
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser] #TODO : Make new permission class so only admin/department manager can see all users and users can only see themselves

    def perform_update(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = User.objects.filter(is_deleted=False)

        department_id = self.request.query_params.get('department')
        work_center_id = self.request.query_params.get('work_center')
        or_condition = self.request.query_params.get('or_condition')  # Set to any value to enable OR logic

        if department_id and work_center_id:
            if not Department.objects.filter(id=department_id).exists() or not WorkCenter.objects.filter(id=work_center_id).exists():
                return Response({"error": "Invalid department or work center id"}, status=status.HTTP_400_BAD_REQUEST)

            if or_condition:
                # OR logic: Retrieve objects matching either department or work_center
                queryset = queryset.filter(Q(workcenter__department__id=department_id) | Q(work_center__id=work_center_id))
            else:
                # AND logic: Retrieve objects matching both department and work_center
                queryset = queryset.filter(department=department_id, work_center=work_center_id)
        elif department_id:
            if not Department.objects.filter(id=department_id).exists():
                return Response({"error": "Invalid department id"}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.filter(workcenter__department__id=department_id)
        elif work_center_id:
            if not WorkCenter.objects.filter(id=work_center_id).exists():
                return Response({"error": "Invalid work center id"}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.filter(work_center__id=work_center_id)

        return queryset
    

def create_token(user_id:int)-> str:
    payload = dict(
        id=user_id,
        exp= datetime.datetime.utcnow() + datetime.timedelta(hours=3) ,
        iat= datetime.datetime.utcnow()
    )
    
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return token
