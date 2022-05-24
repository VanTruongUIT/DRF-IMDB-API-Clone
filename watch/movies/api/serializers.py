from wsgiref.validate import validator
from xml.parsers.expat import model
from django.forms import IntegerField
from rest_framework import serializers

from movies.models import Movies


def validate_length_of_field(value):
    if len(value) < 2:
        raise serializers.ValidationError("Length of field too short!!!")
class MoviesSerializer(serializers.ModelSerializer):
    
    movie_name_length = serializers.SerializerMethodField()
    class Meta:
        model = Movies 
        fields = "__all__"        
        
    def get_movie_name_length(self, object):
        return len(object.movie_name)
    
    # Field level validation function start with validate_<field_name> look like below
    def validate_movie_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("The movie name is too short!!!")
        else:
            return value 
        
    # Validate with object-level
    def validate(self, attrs):
        if (attrs.get('movie_name') == attrs.get('description')):
            raise serializers.ValidationError("The movie name and description should not be same!!!")
        else:
            return attrs