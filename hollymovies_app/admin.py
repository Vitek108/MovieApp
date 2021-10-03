from django.contrib import admin
from .models import Genre, Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]

admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Genre, GenreAdmin)