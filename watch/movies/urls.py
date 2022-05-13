from django.urls import path


from .views import get_all_movies, get_detail_movies


urlpatterns = [
    path("list/", get_all_movies, name="movie-list"),   
    path("<int:pk>", get_detail_movies, name="movie-detail"),   
]



