from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import Comment, Genre, Review, Theme, Movie
from rest_framework.relations import SlugRelatedField


class GenreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = ('unique_id', 'name')


class ThemeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Theme
		fields = ('name',)


class CommentSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)

	class Meta:
		model = Comment
		fields = '__all__'
		read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	comments = CommentSerializer(many=True, read_only=True)
	like_users = UserSerializer(many=True, read_only=True)
	like_count = serializers.IntegerField(
		source='like_users.count',
		read_only=True
	)

	class Meta:
		model = Review
		fields = '__all__'
		read_only_fields = ('movie', 'user', 'like_users')


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

