import json

class MovieCollection:
    def __init__(self, filename):
        self.filename = filename
        self.movies = []

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            self.movies = []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.movies, file, indent=2)

    def add_movie(self, title, director, year, genre):
        movie = {
            'название': title,
            'режиссер': director,
            'год': year,
            'жанр': genre
        }
        self.movies.append(movie)
        self.save_data()

    def list_movies(self):
        return self.movies

    def search_by_title(self, title):
        for movie in self.movies:
            if title.lower() in movie['название'].lower():
                yield movie

    def search_by_director(self, director):
        for movie in self.movies:
            if director.lower() in movie['режиссер'].lower():
                yield movie

    def search_by_year(self, year):
        for movie in self.movies:
            if str(year) == movie['год']:
                yield movie

    def search_by_genre(self, genre):
        for movie in self.movies:
            if genre.lower() in movie['жанр'].lower():
                yield movie
