from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres = movie.genres.all()
    similar_movies = movie.get_similar_movies()[:10]
    context = {
        'movie': movie,
        'similar_movies': similar_movies,
    }
    return render(request, 'movies/recommended.html', context)