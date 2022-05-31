from dataclasses import fields
from wsgiref.validate import validator
from xml.parsers.expat import model
from django.forms import IntegerField
from rest_framework import serializers

from movies.models import StreamPlatform, WatchList, Review


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        exclude = ('watchlist', )


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList 
        fields = "__all__"        
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    # this field name is the related_name in the WatchList models.py
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"