from django.urls import path
from .views import ActorDetailView, ChangePasswordView, CreateActorView, CreateMovieView, DeleteMovieView, \
    GenreDetailView, HomepageView, LoginView, LogoutView, MovieDetailView, ContactView, RegistrationView, \
    UpdateMovieView, PremiumView

urlpatterns = [
    path('homepage/', HomepageView.as_view(), name='homepage'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('genre/<str:genre_name>/', GenreDetailView.as_view(), name='genre_detail'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor_detail'),
    path("contact/", ContactView.as_view(), name="contact"),
    path('create_movie/', CreateMovieView.as_view(), name='create_movie'),
    path("create_actor", CreateActorView.as_view(), name="create_actor"),
    path("update_movie/<int:pk>/", UpdateMovieView.as_view(), name="update_movie"),
    path("delete_movie/<int:pk>/", DeleteMovieView.as_view(), name="movie_delete"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("premium/", PremiumView.as_view(), name="premium"),
]