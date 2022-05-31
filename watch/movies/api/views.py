from xml.dom import NotFoundErr

from django.shortcuts import get_object_or_404
from movies.models import StreamPlatform, WatchList
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets

from structlog import get_logger

from movies.models import Review

from .serializers import ReviewSerializer, StreamPlatformSerializer, WatchListSerializer



log = get_logger()
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        # get pk from url of movie
        pk = self.kwargs.get('pk')
        # get the movie that have pk is pk
        
        watchlist = WatchList.objects.get(pk=pk)
        log.msg(f"truongtv16: {watchlist}")

        serializer.save(watchlist=watchlist)

class ReviewList(generics.ListAPIView):
    """Using concrete Class base view to handle the get, post, update, delete request quickly
    If you want to customize your code, you can override it"""
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        # get pk from url in browser, it mapping with <int:pk>
        pk = self.kwargs.get("pk")
        # Get all review which have the watchlist is the pk
        reviews = Review.objects.filter(watchlist=pk)
        
        return reviews
    
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    log.msg(f"truongtv16 - queryset: {queryset}")
    serializer_class = ReviewSerializer


class WatchListList(APIView):
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
    
    
class StreamFlatformList(APIView):
    def get(self, request):
        stream_flatform = StreamPlatform.objects.all()

        serializers = StreamPlatformSerializer(stream_flatform, many=True, context={'request': request})
        return Response(serializers.data)


    def post(self, request):
        # Get data from field which from client input. After that serializer it
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       


class StreamPlatformDetail(APIView):
    
    def get(self, request, pk):
        try:
            stream_flatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        
        if request.method == "GET":
            serializer = StreamPlatformSerializer(stream_flatform, context={'request': request})
            return Response(serializer.data)
    
    def put(self, request, pk):
        stream_flatform = StreamPlatform.objects.get(pk=pk)

        serializer = StreamPlatformSerializer(stream_flatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk):
        stream_flatform = StreamPlatform.objects.get(pk=pk)
        stream_flatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      


# class StreamPlatformViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         streamplatform = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(streamplatform, context={'request': request})
#         return Response(serializer.data)    

class StreamPlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer    