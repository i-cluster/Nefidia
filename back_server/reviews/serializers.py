from accounts.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Genre, Review, Theme, Movie
from rest_framework.relations import SlugRelatedField


class GenreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = ('unique_id', 'name')


class ThemeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Theme
		fields = ('name',)


class ReviewSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)

	class Meta:
		model = Review
		fields = '__all__'
		read_only_fields = ('movie', 'user',)


class MovieSerializer(serializers.ModelSerializer):
	reviews = ReviewSerializer(many=True, read_only=True)
	unique_id = serializers.IntegerField(read_only=True)
	# movie_genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field='unique_id')
	# movie_themes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
	movie_genres = GenreSerializer(many=True, read_only=True)
	movie_themes = ThemeSerializer(many=True, read_only=True)

	class Meta:
		model = Movie
		fields = '__all__'

