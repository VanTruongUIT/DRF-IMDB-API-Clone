from django.urls import path


# from .views import get_all_movies, get_detail_movies
from .views import DetailMovie, ListMovies


urlpatterns = [
    path("list/", ListMovies.as_view(), name="movie-list"),   
    path("<int:pk>", DetailMovie.as_view(), name="movie-detail"),   
]



