from django.contrib import admin
from movies.models import Movies

class MoviesAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Movies, MoviesAdmin)