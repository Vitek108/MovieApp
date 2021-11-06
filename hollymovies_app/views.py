from django.http import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse_lazy
from django.template.response import TemplateResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, DetailView, FormView, CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import BaseDeleteView, DeleteView, FormMixin
from hollymovies_app.forms import ActorForm, ContactForm, MovieForm, RegistrationForm
from hollymovies_app.models import (
    Movie,
    Genre,
    GENRE_NAME_TO_NAME_SHORTCUT_MAPPING,
    Actor,
)
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


class PremiumView(PermissionRequiredMixin, TemplateView):
    template_name = "premium.html"
    permission_required = "general_permission.can_view_premium_page"


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("homepage")


class LoginView(FormMixin, TemplateView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            # TODO add messages
            return redirect("login")

        login(request, user)
        return redirect("homepage")


class ChangePasswordView(PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("homepage")


class RegistrationView(FormMixin, TemplateView):
    template_name = "accounts/register.html"
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        bounded_form = self.form_class(request.POST)
        if bounded_form.is_valid():
            bounded_form.save()
            return redirect("homepage")
        else:
            return TemplateResponse(request, "accounts/register.html", context={"form": bounded_form})


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


class MovieDetailView(LoginRequiredMixin, View):
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


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "contact_form": ContactForm
        }
        return TemplateResponse(request, "contact.html", context=context)

    def post(self, request, *args, **kwargs):
        bounded_contact_form = ContactForm(request.POST)
        if not bounded_contact_form.is_valid():
            context = {
                "contact_form": bounded_contact_form
            }
            return TemplateResponse(request, "contact.html", context=context)

        name = bounded_contact_form.cleaned_data["name"]
        email = bounded_contact_form.cleaned_data["email"]
        subject = bounded_contact_form.cleaned_data["subject"]
        description = bounded_contact_form.cleaned_data["description"]

        print(name)
        print(email)
        print(subject)
        print(description)

        return redirect("contact")


class CreateActorView(CreateView):
    template_name = "create_actor.html"
    form_class = ActorForm
    model = Actor

    def get_success_url(self) -> str:
        return resolve_url("actor_detail", pk=self.object.id)


class EditMovieMixin:
    template_name = 'create_movie.html'
    form_class = MovieForm
    model = Movie

    def get_success_url(self):
        return resolve_url('movie_detail', pk=self.object.id)


class CreateMovieView(EditMovieMixin, CreateView):
    pass


class UpdateMovieView(EditMovieMixin, UpdateView):
    pass


class DeleteMovieView(BaseDeleteView):
    model = Movie

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return resolve_url("homepage")
