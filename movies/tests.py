from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Movie, Genre
import json

class MovieViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com'
        }
        self.admin_user = User.objects.create_superuser(username='admin', password='avi@123', email='avi@gmail.com')
        self.regular_user = User.objects.create_user(username='user', password='test@123', email='test@gmail.com')
        self.genre = Genre.objects.create(name='Action')
        self.movie = Movie.objects.create(name='Inception', director='Christopher Nolan', imdb_score=8.8, imdb_popularity=90.0)
        self.movie.genres.add(self.genre)

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        print(refresh)
        return str(refresh.access_token)

    def test_admin_can_add_movie(self):
        token = self.get_token_for_user(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'name': 'The Dark Knight',
            'director': 'Christopher Nolan',
            'imdb_score': 9.0,
            'imdb_popularity': 95.0,
            'genre_ids': [self.genre.id]
        }
        response = self.client.post(reverse('movie-list-create'), data=json.dumps(data), content_type='application/json')
        # Print the status code and content for debugging
        print(response.status_code)
        print(response.content)
        
        self.assertEqual(response.status_code, 201)

    def test_regular_user_cannot_add_movie(self):
        token = self.get_token_for_user(self.regular_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'name': 'The Dark Knight',
            'director': 'Christopher Nolan',
            'imdb_score': 9.0,
            'imdb_popularity': 95.0,
            'genre_ids': [self.genre.id]
        }
        response = self.client.post(reverse('movie-list-create'), data=json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Movie.objects.count(), 1)

    def test_admin_can_update_movie(self):
        token = self.get_token_for_user(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'name': 'The Dark Knight',
            'director': 'Christopher Nolan',
            'imdb_score': 9.0,
            'imdb_popularity': 95.0,
            'genre_ids': [self.genre.id]
        }
        response = self.client.put(reverse('movie-detail', args=[self.movie.id]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.name, 'Inception Updated')

    def test_regular_user_cannot_update_movie(self):
        token = self.get_token_for_user(self.regular_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'name': 'The Dark Knight',
            'director': 'Christopher Nolan',
            'imdb_score': 9.0,
            'imdb_popularity': 95.0,
            'genre_ids': [self.genre.id]
        }
        response = self.client.put(reverse('movie-detail', args=[self.movie.id]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 403)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.name, 'Inception')

    def test_admin_can_delete_movie(self):
        token = self.get_token_for_user(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.delete(reverse('movie-detail', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Movie.objects.count(), 0)

    def test_regular_user_cannot_delete_movie(self):
        token = self.get_token_for_user(self.regular_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.delete(reverse('movie-detail', args=[self.movie.id]))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Movie.objects.count(), 1)

    def test_any_user_can_view_movies(self):
        response = self.client.get(reverse('movie-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_any_user_can_search_movies(self):
        response = self.client.get(reverse('movie-list-create'), {'search': 'Inception'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Inception')