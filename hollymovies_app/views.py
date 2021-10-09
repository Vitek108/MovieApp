from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from hollymovies_app.models import (
    Movie,
    Genre,
    GENRE_NAME_TO_NAME_SHORTCUT_MAPPING,
    Actor,
)
from django.views import View


"""def homepage(request):
    movies_db = Movie.objects.all().order_by("-likes", "name")
    context = {
        "movies": movies_db,
    }
    return TemplateResponse(request, "homepage.html", context=context) """

class HomepageView(TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = "homepage.html"
        extra_context = {
            "movies": Movie.objects.all().order_by("-likes", "name")
        }
        return TemplateResponse(request, "homepage.html", context=extra_context)
    
"""     def get(self, request, *args, **kwargs):
        movies_db = Movie.objects.all().order_by("-likes", "name")
        context = {
            "movies": movies_db,
        }
        return TemplateResponse(request, "homepage.html", context=context) """


""" def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == "POST":
        movie.likes += 1
        movie.save()
    context = {
        "movie": movie,
    }
    return TemplateResponse(request, "detail/movie_detail.html", context=context) """

class MovieDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        movie = Movie.objects.get(id=pk)
        context = {
            "movie": movie,
        }
        return TemplateResponse(request, "detail/movie_detail.html", context=context)

    def post(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        movie.likes += 1
        movie.save()
        return self.get(request, pk, *args, **kwargs)



""" def genre_detail(request, genre_name):
    genre_name_shortcut = GENRE_NAME_TO_NAME_SHORTCUT_MAPPING[genre_name]
    genre = Genre.objects.get(name=genre_name_shortcut)
    context = {"genre": genre}
    return TemplateResponse(request, "detail/genre_detail.html", context=context) """
    
class GenreDetailView(View):
    def get(self, request, genre_name, *args, **kwargs):
        genre_name_shortcut = GENRE_NAME_TO_NAME_SHORTCUT_MAPPING[genre_name]
        genre = Genre.objects.get(name=genre_name_shortcut)
        context = {"genre": genre}
        return TemplateResponse(request, "detail/genre_detail.html", context=context)


""" def actor_detail(request, pk):
    actor = Actor.objects.get(id=pk)
    context = {
        "actor": actor,
    }
    return TemplateResponse(request, "detail/actor_detail.html", context=context) """


class ActorDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        actor = Actor.objects.get(id=pk)
        context = {
            "actor": actor,
        }
        return TemplateResponse(request, "detail/actor_detail.html", context=context)