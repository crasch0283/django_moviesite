import os
import shutil
import tempfile
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.conf import settings

from .models import Movie
from .forms import MovieForm

class MovieModelTests(TestCase):
    def setUp(self):
        # Create a temporary directory for media files
        self.media_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.media_dir, ignore_errors=True)

    def create_image(self, name='test.jpg'):
        return SimpleUploadedFile(name, b'filecontent', content_type='image/jpeg')

    def test_movie_creation(self):
        with self.settings(MEDIA_ROOT=self.media_dir):
            movie = Movie.objects.create(
                title='Test Movie',
                director='Director',
                yearReleased='2022',
                movieImg=self.create_image()
            )
            self.assertEqual(Movie.objects.count(), 1)
            self.assertEqual(movie.title, 'Test Movie')

class MovieFormTests(TestCase):
    def setUp(self):
        self.media_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.media_dir, ignore_errors=True)

    def create_image(self, name='form.jpg'):
        return SimpleUploadedFile(name, b'image', content_type='image/jpeg')

    def test_movie_form_valid(self):
        form = MovieForm(data={
            'title': 'Valid Title',
            'director': 'Someone',
            'yearReleased': '2020'
        }, files={'movieImg': self.create_image()})
        self.assertTrue(form.is_valid())

    def test_movie_form_invalid_short_title(self):
        form = MovieForm(data={
            'title': 'ab',
            'director': 'Dir',
            'yearReleased': '2020'
        }, files={'movieImg': self.create_image('short.jpg')})
        self.assertFalse(form.is_valid())

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.media_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.media_dir, ignore_errors=True)

    def create_movie(self):
        with self.settings(MEDIA_ROOT=self.media_dir):
            return Movie.objects.create(
                title='Search Movie',
                director='Dir',
                yearReleased='2020',
                movieImg=SimpleUploadedFile('search.jpg', b'img', content_type='image/jpeg')
            )

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_searchmovies_found(self):
        self.create_movie()
        response = self.client.post(reverse('searchmovies'), {'title': 'Search Movie'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/searchmovies.html')

    def test_searchmovies_not_found(self):
        response = self.client.post(reverse('searchmovies'), {'title': 'Nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/movienotfound.html')

