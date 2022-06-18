from django.db import models
from django.forms import CharField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.contrib.auth.models import User


class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=200)
    storyline = models.CharField(max_length=200)
    # Add foreign key to StreamPlatform: one to many relationship.
    stream_platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=255, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{str(self.rating)} | {self.watchlist.title} | {self.author}" 
