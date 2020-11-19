from django.shortcuts import render

from reviews.tmdb import url

# Create your views here.


def index(request):
    
    return render(request, 'index.html')