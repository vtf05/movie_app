from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    director = models.CharField(max_length=100)
    imdb_score = models.FloatField()
    imdb_popularity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField('Genre', through='MovieGenre')

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['name'], name='name_idx')
        ]
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.movie.name} - {self.genre.name}'