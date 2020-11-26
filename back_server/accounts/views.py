from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from reviews.models import Genre, Theme

from .serializers import UserSerializer

# Create your views here.

User = get_user_model()

@api_view(['POST'])
def signup(request):
	password = request.data.get('password')
	password_confirm = request.data.get('passwordConfirmation')
	
	if password != password_confirm:
		return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
	
	user_genres = []
	for (key, value) in request.data.pop('user_genres').items():
		if value:
			user_genres.append(Genre.objects.get(unique_id=key))

	user_themes = []
	for (key, value) in request.data.pop('user_themes').items():
		if value:
			user_themes.append(Theme.objects.get(name=key))

	user_serializer = UserSerializer(data=request.data)

	if user_serializer.is_valid(raise_exception=True):
		user = user_serializer.save(user_genres=user_genres, user_themes=user_themes)
		user.set_password(request.data.get('password'))
		user.save()

	return Response(user_serializer.data, status=status.HTTP_201_CREATED)