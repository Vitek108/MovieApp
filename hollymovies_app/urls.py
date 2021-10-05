from django.urls import path
from .views import homepage, movie_detail, genre_detail, actor_detail


urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('movie/<int:pk>/', movie_detail, name="movie_detail"),
    path('genre/<str:genre_name>/', genre_detail, name='genre_detail'),
    path('actor/<int:pk>/', actor_detail, name='actor_detail'),
]