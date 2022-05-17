from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from movies.models import Movies
from .serializers import MoviesSerializer


class ListMovies(APIView):
    def get(self, request):
        movies = Movies.objects.all()

        serializers = MoviesSerializer(movies, many=True)
        return Response(serializers.data)


    def post(self, request):
        # Get data from field which from client input. After that serializer it
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       



class DetailMovie(APIView):
    
    def get(self, request, pk):
        try:
            movie = Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        
        if request.method == "GET":
            serializer = MoviesSerializer(movie)
            return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Movies.objects.get(pk=pk)

        serializer = MoviesSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk):
        movie = Movies.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)          