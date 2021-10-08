from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from hollymovies_app.models import Movie, Genre, GENRE_NAME_TO_NAME_SHORTCUT_MAPPING, Actor


def homepage(request):
    movies_db = Movie.objects.all().order_by("-likes", "name")
    context = {
        "movies": movies_db,
    }
    return TemplateResponse(request, "homepage.html", context=context)

def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == "POST":
        movie.likes += 1
        movie.save()
        
    context = {
        "movie": movie,
    }
    return TemplateResponse(request, "detail/movie_detail.html", context=context)

    

def genre_detail(request, genre_name):
    genre_name_shortcut = GENRE_NAME_TO_NAME_SHORTCUT_MAPPING[genre_name]
    genre = Genre.objects.get(name=genre_name_shortcut)
    context = {
        'genre': genre
    }
    return TemplateResponse(request, 'detail/genre_detail.html', context=context)

def actor_detail(request, pk):
    actor = Actor.objects.get(id=pk)
    context = {
        "actor": actor,
    }
    return TemplateResponse(request, "detail/actor_detail.html", context=context)