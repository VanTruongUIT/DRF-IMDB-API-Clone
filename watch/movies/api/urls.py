from django.urls import path


# from .views import get_all_movies, get_detail_movies
from .views import (
    WatchListList, 
    WatchListDetail, 
    StreamFlatformList, 
    StreamPlatformDetail,
    ReviewList,
    ReviewDetail,
)


urlpatterns = [
    path("list/", WatchListList.as_view(), name="watchlist-list"),
    path("list/<int:pk>", WatchListDetail.as_view(), name="watchlist-detail"),
    path("stream-platforms/", StreamFlatformList.as_view(), name="streamplatform-list"),
    path("stream-platforms/<int:pk>", StreamPlatformDetail.as_view(), name="streamplatform-detail"),
    path("list/reviews/", ReviewList.as_view(), name="review-list"),
    path("list/<int:pk>/reviews/", ReviewDetail.as_view(), name="review-detail"),
]



