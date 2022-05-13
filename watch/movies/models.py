from django.db import models
from django.forms import CharField

class Movies(models.Model):
    movie_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.movie_name