from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from movies.models import Movies
from .serializers import MoviesSerializer

@api_view(["GET", "POST"])
def get_all_movies(request):
    if request.method == "GET":
        movies = Movies.objects.all()

        serializers = MoviesSerializer(movies, many=True)
        return Response(serializers.data)
    
    elif request.method == "POST":
        # Get data from field which from client input. After that serializer it
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def get_detail_movies(request, pk):
    
    try:
        movie = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    if request.method == "GET":
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 