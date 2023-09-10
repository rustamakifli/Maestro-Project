from django.contrib.auth import get_user_model
from users.api.serializers import MyUserSerializer,UserDetail
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from  rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from users.utils import jwt
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
    
class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = super().post( request, *args, **kwargs)
        data = data.data
        access_token = jwt.jwt_decode_handler(data.get("access"))
        user = User.objects.filter(email=access_token.get("email")).first()

        if not user:
            return Response({"error":True, "message":"Check password or email"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserDetail(user)
        data["user"] = serializer.data
        return Response(data)    
    
class RefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        data = data.data
        return Response(data)