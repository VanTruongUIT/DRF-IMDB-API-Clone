from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status

# from users import models

@api_view(["POST"])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        
        return Response(status=status.HTTP_200_OK)
        

@api_view(["POST", ])
def register_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        print(f'serializer {serializer}')
        
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            
            data['response'] = 'Registration successful!'
            data['username'] = user.username
            data['email'] = user.email
            
            token = Token.objects.get(user=user).key
            data['token'] = token 
            
            
        else:
            data = serializer.errors
            
        print(data)
        return Response(data)