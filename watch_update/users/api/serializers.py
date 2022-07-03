from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    # password2 write_only means you cannot read the password
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User 
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError (
                {'Error': 'p1 and p2 should be the same!'}
            )
            
        user_query = User.objects.filter(email=self.validated_data['email'])
        if user_query.exists():
            raise serializers.ValidationError(
                {'Error': 'Email already exists!'}
            )
        
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        user.set_password(password)
        
        user.save()
        
        return user