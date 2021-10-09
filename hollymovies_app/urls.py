from django.urls import path
from .views import ActorDetailView, GenreDetailView, HomepageView, MovieDetailView


urlpatterns = [
    path('homepage/', HomepageView.as_view(), name='homepage'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('genre/<str:genre_name>/', GenreDetailView.as_view(), name='genre_detail'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor_detail'),
]