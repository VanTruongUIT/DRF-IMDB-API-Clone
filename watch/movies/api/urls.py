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
    path("list/<int:pk>", DetailWatchList.as_view(), name="watchlist-detail"),   
    path("stream-platforms/", ListStreamFlatform.as_view(), name="streamplatform-list"),   
    path("stream-platforms/<int:pk>", DetaiStreamPlatform.as_view(), name="streamplatform-detail"),   
]



