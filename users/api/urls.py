from django.urls import path
from users.api.views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),

]