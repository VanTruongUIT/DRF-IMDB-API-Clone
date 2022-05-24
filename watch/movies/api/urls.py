from django.urls import path


# from .views import get_all_movies, get_detail_movies
from .views import (
    ListWatchList, 
    DetailWatchList, 
    ListStreamFlatform, 
    DetaiStreamPlatform,
)


urlpatterns = [
    path("list/", ListWatchList.as_view(), name="watchlist-list"),   
    path("<int:pk>", DetailWatchList.as_view(), name="watchlist-detail"),   
    path("stream-flatforms/", ListStreamFlatform.as_view(), name="streamflatform-list"),   
    path("stream-flatforms/<int:pk>", DetaiStreamPlatform.as_view(), name="streamflatform-detail"),   
]



