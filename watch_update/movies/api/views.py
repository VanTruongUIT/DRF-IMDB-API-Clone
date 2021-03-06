from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from movies.api.paginations import (WatchListCursorPagination,
                                    WatchListPageNumberPagination)
from movies.models import Review, StreamPlatform, WatchList
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.validators import ValidationError
from rest_framework.views import APIView
from structlog import get_logger

from .permisstions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import (ReviewSerializer, StreamPlatformSerializer,
                          WatchListSerializer)
from .throttling import ReviewCreateThrottle, ReviewListThrottle

log = get_logger()


class UserReviewList(generics.ListAPIView):
    """Using ListAPIView"""
    serializer_class = ReviewSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        reviews = Review.objects.filter(author__username=username)
        
        return reviews


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    permission_classes = [IsAuthenticated]
    
    throttle_classes = [ReviewCreateThrottle]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        # get pk from url of movie
        pk = self.kwargs.get('pk')
        # get the movie that have pk is pk
        
        watchlist = WatchList.objects.get(pk=pk)
        # log.msg(f"truongtv16: {watchlist}")
        
        # check if the user already have the review for the moview -> we will not create a new review
        current_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, author=current_user)
        
        if review_queryset.exists():
            raise ValidationError("You already have one review for this movie! You can not add new one!")
        if watchlist.number_of_ratings == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2            
        watchlist.number_of_ratings += 1
        
        watchlist.save()

        serializer.save(watchlist=watchlist, author=current_user)
    

class ReviewList(generics.ListAPIView):
    """Using concrete Class base view to handle the get, post, update, delete request quickly
    If you want to customize your code, you can override it"""
    serializer_class = ReviewSerializer
    # if you're login -> you have permission to create a new object, If not, you only can view 
    # permission_classes = [IsAuthorOrReadOnly]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('author__username', 'active')    

    def get_queryset(self):
        # get pk from url in browser, it mapping with <int:pk>
        pk = self.kwargs.get("pk")
        # Get all review which have the watchlist is the pk
        reviews = Review.objects.filter(watchlist=pk)
        
        return reviews

    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    # log.msg(f"truongtv16 - queryset: {queryset}")
    serializer_class = ReviewSerializer
    # if you're login -> you have permission to create a new object, If not, you only can view 
    permission_classes = [IsAuthorOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class WatchListGenericsList(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    # pagination_class = WatchListPageNumberPagination
    pagination_class = WatchListCursorPagination


class WatchListList(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        watch_list = WatchList.objects.all()

        serializers = WatchListSerializer(watch_list, many=True)
        return Response(serializers.data)


    def post(self, request):
        # Get data from field which from client input. After that serializer it
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       


class WatchListDetail(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        
        if request.method == "GET":
            serializer = WatchListSerializer(watch_list)
            return Response(serializer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)

        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk):
        watch_list = WatchList.objects.get(pk=pk)
        watch_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


class StreamPlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer   
    permission_classes = [IsAdminOrReadOnly]
     