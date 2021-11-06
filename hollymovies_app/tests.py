
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from hollymovies_app.models import Movie
from hollymovies_app.views import HomepageView, GenreDetailView


class TestUrls(SimpleTestCase):
    def test_homepage_url_is_resolved(self):
        url = reverse("homepage")
        self.assertEqual(resolve(url).func.view_class, HomepageView)

    def test_genre_detail_url_is_resolved(self):
        url = reverse("genre_detail", args=["testing_genre"])
        self.assertEqual(resolve(url).func.view_class, GenreDetailView)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(name="Testing Movie")


    def test_homepage_GET(self):
        url = reverse("homepage")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "homepage.html")

    def test_movie_detail_GET(self):
        url = reverse("movie_detail", args=[9999999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)