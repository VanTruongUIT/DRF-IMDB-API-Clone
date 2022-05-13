from rest_framework.response import Response
from rest_framework.decorators import api_view

from movies.models import Movies
from .serializers import MoviesSerializer

@api_view()
def get_all_movies(request):
    movies = Movies.objects.all()

    serializers = MoviesSerializer(movies, many=True)
    return Response(serializers.data)

@api_view()
def get_detail_movies(request, pk):
    movie = Movies.objects.get(pk=pk)

    serializer = MoviesSerializer(movie)
    return Response(serializer.data)