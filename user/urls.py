from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserViewSet, UserRfidLoginView

urlpatterns = [
    # Register a new user
    path('register/', UserRegistrationView.as_view(), name='register'),

    # Login using email and password
    path('login/', UserLoginView.as_view(), name='login'),

    # Logout the currently authenticated user
    path('logout/', UserLogoutView.as_view(), name='logout'),

    # List all users or create a new user
    path('user/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),

    # Retrieve, update or delete a specific user
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),

    # Login using RFID UID
    path('rfid-login/', UserRfidLoginView.as_view(), name='rfid-login'),
]
