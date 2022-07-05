from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import (
    UserReviewList,
    WatchListList, 
    WatchListDetail, 
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    StreamPlatformViewSet,
    WatchListGenericsList
)

router = DefaultRouter()
router.register("stream-platforms", StreamPlatformViewSet, basename="streamplatform")

urlpatterns = [
    path("", WatchListList.as_view(), name="watchlist_list"),
    path("generics-list/", WatchListGenericsList.as_view(), name="watchlist_generics_list"),
    path("<int:pk>/", WatchListDetail.as_view(), name="watchlist_detail"),
    
    path("", include(router.urls)),

    path("<int:pk>/reviews/create/", ReviewCreate.as_view(), name="review_create"),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review_list"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="review_detail"),
    
    path("reviews/", UserReviewList.as_view(), name="user_review_list"),
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]


