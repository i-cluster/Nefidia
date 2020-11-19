class Movie_url:
    
    url = 'https://api.themoviedb.org/3/movie/550'
    key = ''


    def __init__(self, key):
        self.key = key

    def get_url(self, category='boxoffice', feature='searchWeeklyBoxOfficeList'):
        return f'{self.url}?api_key={self.key}'

url = Movie_url('d2d2eae7df4acbf670c97c4309b85835')
print(url.get_url())
