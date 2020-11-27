import re
import requests
import json
from copy import deepcopy

from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Genre, Review, Theme, Movie
from .serializers import CommentSerializer, GenreSerializer, ThemeSerializer, MovieSerializer, ReviewSerializer

# Create your views here.

class Movie_url:
    
    url = 'https://api.themoviedb.org/3/movie'
    key = ''

    def __init__(self, key):
        self.key = key

    def get_movie_filtered_url(self, filt, pageNum, lang="ko-KR"):
        return f'{self.url}/{filt}/?api_key={self.key}&page={pageNum}&language={lang}'


# 영화 등록
@api_view(['GET'])
def movie_register(request):
    # 유저의 관심 장르
    genres = Genre.objects.all()
    genre_serializer = GenreSerializer(genres, many=True)

    # 유저의 관심 테마
    themes = Theme.objects.all()
    theme_serializer = ThemeSerializer(themes, many=True)
    # api 영화 정보 받기
    filter_code = ['top_rated', 'upcoming', 'popular', 'now_playing']
    # filter_code = ['top_rated']
    movies_db = {code: [] for code in filter_code}

    movies_ids = Movie.objects.values_list('unique_id', flat=True)

    for code in filter_code:
        for i in range(1, 2):
            popular_url = Movie_url('d2d2eae7df4acbf670c97c4309b85835').get_movie_filtered_url(code, i)
            get_movies = requests.get(popular_url).json()
            # Vue State에 보내기
            movies = deepcopy(get_movies['results'])
            movies_db[code].extend(movies)
            # 영화 DB에 저장하기
            for movie in get_movies['results']:
                if movie['id'] not in movies_ids:
                    unique_id = movie.pop('id')
                    genre_ids = movie.pop('genre_ids')
                    movie_genres = []
                    for genre_id in genre_ids:
                        movie_genres.append(Genre.objects.get(unique_id=genre_id))

                    for field in ['video', 'vote_count', 'original_title', 'original_language']:
                        movie.pop(field)

                    movie_serializer = MovieSerializer(data=movie)
                    if movie_serializer.is_valid(raise_exception=True):
                        movie_serializer.save(unique_id=unique_id, movie_genres=movie_genres)

    
    return Response({'genres': genre_serializer.data, 'themes': theme_serializer.data, 'movies_db': movies_db, 'filter_code': filter_code})


# 페이지 빌드업
@api_view(['GET'])
def build(request):
    # 유저의 관심 장르
    

    # 유저의 관심 테마
    

    # 전체 영화 정보

    return Response()



@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request):
    movie_id = request.GET.get('movieId')
    movie = get_object_or_404(Movie, unique_id=movie_id)
    movie_serializer = MovieSerializer(movie)

    reviews = movie.reviews.all()
    reviews_serializer = ReviewSerializer(reviews, many=True)
    print(reviews.values())

    try:
        review = reviews.get(user=request.user)
        review_serializer = ReviewSerializer(review)
    except:
        review_serializer = ReviewSerializer()

    user_like_reviews = request.user.like_reviews.all()
    print(user_like_reviews)


    return Response({'movie': movie_serializer.data, 'reviews': reviews_serializer.data, 'user_review': review_serializer.data})


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request, movie_id):
    movie = get_object_or_404(Movie, unique_id=movie_id)
    review_serializer = ReviewSerializer(data=request.data)
    if review_serializer.is_valid(raise_exception=True):
        review_serializer.save(movie=movie, user=request.user)
    return Response(review_serializer.data)


@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def edit(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if not request.user.reviews.filter(pk=review_id).exists():
        return Response({'detail': '권한이 없습니다.'})
    
    review_serializer = ReviewSerializer(review, data=request.data)
    if review_serializer.is_valid(raise_exception=True):
        review_serializer.save()
        return Response(review_serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    comment_serializer = CommentSerializer(data=request.data)
    if comment_serializer.is_valid(raise_exception=True):
        comment_serializer.save(review=review, user=request.user)
    return Response(comment_serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request):
    review_id = request.GET.get('reviewId')
    review = get_object_or_404(Review, pk=review_id)
    user = request.user
    # print(review.like_users.all())

    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        liked = False
    else:
        review.like_users.add(user)
        liked = True
    # print(review.like_users.all())

    review_serializer = ReviewSerializer(review)
    print(review_serializer.data.get('id'))
    print(review_serializer.data.get('like_users'))
    print(review_serializer.data.get('like_count'))

    return Response({'review': review_serializer.data, 'liked': liked})