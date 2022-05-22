from wsgiref.validate import validator
from django.forms import IntegerField
from rest_framework import serializers

from movies.models import Movies


def validate_length_of_field(value):
    if len(value) < 2:
        raise serializers.ValidationError("Length of field too short!!!")
class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    movie_name = serializers.CharField()
    description = serializers.CharField(validators=[validate_length_of_field, ])
    active = serializers.BooleanField()
    
    
    def create(self, validated_data):
        return Movies.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.movie_name = validated_data.get("movie_name", instance.movie_name)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance
    
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