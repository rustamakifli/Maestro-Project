from django.urls import path
from users.api.views import UserRegisterView, LoginView, RefreshTokenView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view()),
    path('refresh/', RefreshTokenView.as_view()),
]