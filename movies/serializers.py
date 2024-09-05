from rest_framework import serializers
from .models import Movie, Genre, MovieGenre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, write_only=True)

    class Meta:
        model = Movie
        fields =  ['id', 'name', 'director', 'imdb_score', 'imdb_popularity', 'genres','genre_ids']
        extra_kwargs = {
            'genres': {'read_only': True},
            'genre_ids': {'write_only': True}
        }

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]
    
    def create(self, validated_data):
        genres = validated_data.pop('genre_ids')
        movie = Movie.objects.create(**validated_data)
        for genre in genres:
            MovieGenre.objects.create(movie=movie, genre=genre)
        return movie

    def update(self, instance, validated_data):
        print(validated_data)
        genres = validated_data.pop('genre_ids')
        instance.name = validated_data.get('name', instance.name)
        instance.director = validated_data.get('director', instance.director)
        instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
        instance.imdb_popularity = validated_data.get('imdb_popularity', instance.imdb_popularity)
        instance.save()

        # Clear existing genres and add new ones
        instance.moviegenre_set.all().delete()
        for genre in genres:
            MovieGenre.objects.create(movie=instance, genre=genre)
        return instance

class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = '__all__'