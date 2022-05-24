from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from movies.models import WatchList
from movies.models import StreamPlatform
from .serializers import StreamPlatformSerializer, WatchListSerializer


class ListWatchList(APIView):
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



class DetailWatchList(APIView):
    
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
    
class ListStreamFlatform(APIView):
    def get(self, request):
        stream_flatform = StreamPlatform.objects.all()

        serializers = StreamPlatformSerializer(stream_flatform, many=True)
        return Response(serializers.data)


    def post(self, request):
        # Get data from field which from client input. After that serializer it
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       



class DetaiStreamPlatform(APIView):
    
    def get(self, request, pk):
        try:
            stream_flatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        
        if request.method == "GET":
            serializer = StreamPlatformSerializer(stream_flatform)
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
    
    
    