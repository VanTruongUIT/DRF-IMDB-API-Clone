from wsgiref.validate import validator
from xml.parsers.expat import model
from django.forms import IntegerField
from rest_framework import serializers

from movies.models import StreamPlatform, WatchList


class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList 
        fields = "__all__"        
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"