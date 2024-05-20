from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from apps.User.serializers import AuthorizationSerializer, RegistrationSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout, login
from django.shortcuts import redirect




class AuthorizationViewAPI(APIView):
    def post(self, request):
        try:
            user = get_object_or_404(User, username=request.data['username'])
        except:
             return Response(status=status.HTTP_401_UNAUTHORIZED, data={'Error': 'enter username'})
         
        if not user.check_password(request.data['password']):
            return Response(data={'login': 'wrong username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)
        serializer = AuthorizationSerializer(instance=user)
        login(request, user=user)
        return Response(status=status.HTTP_200_OK, data={'key': token.key, 'user':serializer.data})


class RegistrationViewAPI(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        token = Token.objects.create(user=user)
        return Response(status=status.HTTP_201_CREATED, data={'key': token.key, 'user':serializer.data})

def logout_view(request):
    logout(request)
    return redirect('/user/login/')