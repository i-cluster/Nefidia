from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    unique_id = models.IntegerField()
    name = models.CharField(max_length=50)


class Theme(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    unique_id = models.IntegerField()
    title = models.CharField(max_length=100)
    movie_genres = models.ManyToManyField(Genre, related_name="genre_movies")
    movie_themes = models.ManyToManyField(Theme, related_name="theme_movies")
    overview = models.TextField(blank=True)
    release_date = models.DateField()
    vote_average = models.FloatField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=500, blank=True)
    backdrop_path = models.CharField(max_length=500, blank=True)
    adult = models.BooleanField(default=False)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    vote = models.IntegerField()
    content = models.TextField()
    spoiler = models.BooleanField(default=False)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()