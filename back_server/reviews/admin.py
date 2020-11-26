from django.contrib import admin
from .models import Movie, Genre, Theme, Review, Comment
from accounts.models import User

# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Theme)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)
# admin.site.register(settings.AUTH_USER_MODEL)