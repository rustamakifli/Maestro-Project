from django.contrib.auth import get_user_model
from users.api.serializers import MyUserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

# Create your views here.

class UserRegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data  = request.data
        serializer = MyUserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            data = dict(serializer.data)
            data.pop('password')
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    