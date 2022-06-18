from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response

# from users import models


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
            
            token = Token.objects.get(user=user).key
            data['token'] = token 
            
            
        else:
            data = serializer.errors
            
        print(data)
        return Response(data)