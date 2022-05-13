from django.forms import IntegerField
from rest_framework import serializers 


class MoviesSerializer(serializers.Serializer):
    ID = serializers.IntegerField(read_only=True)
    movie_name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    