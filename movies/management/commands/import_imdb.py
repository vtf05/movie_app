import json
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from movies.models import Movie, Genre

class Command(BaseCommand):
    help = 'Import movies from imdb.json'

    def handle(self, *args, **kwargs):
        with open('imdb.json', 'r') as file:
            data = json.load(file)
        
        for item in data:
            genres = item.pop('genre', [])
            insert_item = {
                'name': item['name'],
                'director': item['director'],
                'imdb_score': item['imdb_score'],
                'imdb_popularity': item['99popularity'],
            }
            try:
                movie, created = Movie.objects.get_or_create(**insert_item)
            except IntegrityError:
                movie = Movie.objects.get(name=insert_item['name'])
                movie.director = insert_item['director']
                movie.imdb_score = insert_item['imdb_score']
                movie.imdb_popularity = insert_item['imdb_popularity']
                movie.save()
                created = False

            for genre_name in genres:
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                movie.genres.add(genre)
            movie.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully imported movies from imdb.json'))