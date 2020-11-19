import requests
import json
from django.shortcuts import render

class Movie_url:
    
    url = 'https://api.themoviedb.org/3/movie'
    key = ''


    def __init__(self, key):
        self.key = key

    def get_movie_filtered_url(self, filt, pageNum, lang="ko-KR"):
        return f'{self.url}/{filt}/?api_key={self.key}&page={pageNum}&language={lang}'

# Create your views here.


def index(request):

    # print(url)
    filter_code = ['top_rated', 'upcoming', 'popular', 'now_playing', 'latest']

    movies_db = {code: [] for code in filter_code}

    for code in filter_code:
        for i in range(1, 3):
            popular_url = Movie_url('d2d2eae7df4acbf670c97c4309b85835').get_movie_filtered_url(code, i)
            get_movies = requests.get(popular_url).json()
            if code != 'latest':
                movies_db[code].extend(get_movies['results'])
            else:
                movies_db[code].extend(get_movies)


    print(movies_db)
    return render(request, 'index.html', {'movies_db': movies_db})