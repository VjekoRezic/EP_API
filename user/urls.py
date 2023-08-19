from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserViewSet

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/', UserViewSet.as_view({'get':'list'}), name='user-list'),
    path('user/<int:pk>/', UserViewSet.as_view({'get':'retrieve'}), name='user-detail'),
]