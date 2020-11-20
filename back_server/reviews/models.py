from django.db import models
from django.db.models.expressions import F

# Create your models here.


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    genre_id = models.IntegerField()
    overview = models.TextField()
    released = models.DateField()
    vote = models.IntegerField()
    poster = models.CharField(max_length=500)
    backdrop = models.CharField(max_length=500)
    adult = models.BooleanField(default=False)