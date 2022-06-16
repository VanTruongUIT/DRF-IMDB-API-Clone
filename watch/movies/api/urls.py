from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

# from .views import get_all_movies, get_detail_movies
from .views import (
    WatchListList, 
    WatchListDetail, 
    StreamFlatformList, 
    StreamPlatformDetail,
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    StreamPlatformViewSet,
)

router = DefaultRouter()
router.register("stream-platforms", StreamPlatformViewSet, basename="streamplatform")

urlpatterns = [
    path("list/", WatchListList.as_view(), name="watchlist-list"),
    path("list/<int:pk>/", WatchListDetail.as_view(), name="watchlist-detail"),
    
    path("", include(router.urls)),
    # path("stream-platforms/", StreamFlatformList.as_view(), name="streamplatform-list"),
    # path("stream-platforms/<int:pk>", StreamPlatformDetail.as_view(), name="streamplatform-detail"),
    
    # path("reviews/", ReviewList.as_view(), name="review-list"),
    # path("reviews/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
    path("<int:pk>/reviews-create/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
    
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]


