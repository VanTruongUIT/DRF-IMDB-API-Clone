# from django.http import JsonResponse
# from django.shortcuts import render

# from movies.models import Movies


# def get_all_movies(request):
#     movies = Movies.objects.all()

#     data = {
#         "movies": list(movies.values())
#     }

#     return JsonResponse(data=data)



# def get_detail_movies(request, pk):
#     movie = Movies.objects.get(pk=pk)
    
#     data = {
#         "name": movie.movie_name ,
#         "description": movie.description,
#         "active": movie.active
#     }
    
#     return JsonResponse(data)