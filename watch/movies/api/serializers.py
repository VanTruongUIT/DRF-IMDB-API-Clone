from django.forms import IntegerField
from rest_framework import serializers

from movies.models import Movies


class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    movie_name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    
    def create(self, validated_data):
        return Movies.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.movie_name = validated_data.get("movie_name", instance.movie_name)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance