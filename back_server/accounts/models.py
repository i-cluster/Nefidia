from django.db import models
from django.contrib.auth.models import AbstractUser
from reviews.models import Genre, Theme

# Create your models here.

class User(AbstractUser):
    user_genres = models.ManyToManyField(Genre, related_name="genre_users")
    user_themes = models.ManyToManyField(Theme, related_name="theme_users")
    followings = models.ManyToManyField('self', symmetrical=False, related_name="followers")