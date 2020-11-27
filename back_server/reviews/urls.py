from django.urls import path
from . import views

urlpatterns = [
    path('movie-register/', views.movie_register),
    path('build/', views.build),
    path('movie-detail/', views.movie_detail),
    path('create/<int:movie_id>/', views.create),
    path('edit/<int:review_id>/', views.edit),
    path('like/', views.like),
    path('comment/create/<int:review_id>/', views.comment_create),
]
