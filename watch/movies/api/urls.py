from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

# from .views import get_all_movies, get_detail_movies
from .views import (
    UserReviewList,
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
    path("list/", WatchListList.as_view(), name="watchlist_list"),
    path("list/<int:pk>/", WatchListDetail.as_view(), name="watchlist_detail"),
    
    path("", include(router.urls)),
    # path("stream-platforms/", StreamFlatformList.as_view(), name="streamplatform-list"),
    # path("stream-platforms/<int:pk>", StreamPlatformDetail.as_view(), name="streamplatform-detail"),
    
    # path("reviews/", ReviewList.as_view(), name="review-list"),
    # path("reviews/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
    path("<int:pk>/reviews-create/", ReviewCreate.as_view(), name="review_create"),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review_list"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="review_detail"),
    # path("reviews/<str:username>/", UserReviewList.as_view(), name="user_review_list"),
    path("reviews/", UserReviewList.as_view(), name="user_review_list"),
    
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]


