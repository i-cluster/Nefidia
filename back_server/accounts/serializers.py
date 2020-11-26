from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.relations import SlugRelatedField

# from reviews.serializers import GenreSerializer, ThemeSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	user_genres = SlugRelatedField(many=True, read_only=True, slug_field='unique_id')
	user_themes = SlugRelatedField(many=True, read_only=True, slug_field='name')
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'password', 'user_genres', 'user_themes',)