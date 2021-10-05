from django.contrib import admin
from .models import Genre, Movie, Actor

class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]

admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Genre, GenreAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ["name"]
                    
admin.site.register(Actor, ActorAdmin)