import requests
import json
from django.shortcuts import render

# Create your views here.

class Movie_url:
    
    url = 'https://api.themoviedb.org/3/movie'
    key = ''


    def __init__(self, key):
        self.key = key

    def get_movie_filtered_url(self, filt, pageNum, lang="ko-KR"):
        return f'{self.url}/{filt}/?api_key={self.key}&page={pageNum}&language={lang}'


def index(request):
    filter_code = ['top_rated', 'upcoming', 'popular', 'now_playing', 'latest']

    movies_db = {code: [] for code in filter_code}

    for code in filter_code:
        if code != 'latest':
            for i in range(1, 2):
                popular_url = Movie_url('d2d2eae7df4acbf670c97c4309b85835').get_movie_filtered_url(code, i)
                get_movies = requests.get(popular_url).json()
                movies_db[code].extend(get_movies['results'][0].keys())

    return render(request, 'index.html', {'movies_db': movies_db.values(), 'code': filter_code})