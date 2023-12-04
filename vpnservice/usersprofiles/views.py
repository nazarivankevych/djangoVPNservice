from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import UserProfile
from .serializers import CustomUserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})
