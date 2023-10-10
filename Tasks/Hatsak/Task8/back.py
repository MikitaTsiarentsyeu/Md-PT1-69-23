import datetime


def year_validation(year):
    CURRENT_YEAR = datetime.datetime.now().year
    FIRST_MOVIE_YEAR = 1895

    if len(str(year)) == 4 and str(year).isdigit() and CURRENT_YEAR >= int(year) >= FIRST_MOVIE_YEAR:
        return int(year)
    else:
        return False


class Movie:

    def __init__(self, name, genre, director, year, ):
        self.name = name.lower().strip()
        self.genre = genre.lower().strip()
        self.director = director.lower().strip()
        if year_validation(year):
            self.year = int(year)
        else:
            self.year = 9999

    def __str__(self):
        _name = self.name.capitalize()
        _dir = self.director.title()
        return f'{_name}, {_dir} - {self.year}, ({self.genre})'

    def __repr__(self):
        _name = self.name.capitalize()
        _dir = self.director.title()
        return f'{_name}, {_dir} - {self.year}, ({self.genre})'

    def __len__(self):
        return 1

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        if self.year == other.year and self.name == other.name and self.genre == self.genre and self.director == self.director:
            return True
        return False

    def __add__(self, other):
        if isinstance(other, Movie):
            coll = Cinematheque()
            coll.append(self)
            coll.append(other)
            return coll
        else:
            raise TypeError("Only Movies are allowed")


class Cinematheque:
    def __init__(self):
        self.collection = []

        self.start = 0
        self.stop = 0
        self.step = 1
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.collection[self.value]
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __getitem__(self, item):
        return self.collection[item]

    def __str__(self):
        return '; '.join([str(movie) for movie in self.collection])

    def append(self, movie):
        if isinstance(movie, Movie):
            self.collection.append(movie)
            self.stop += 1
        else:
            raise TypeError("Only Movies are allowed")

    def __add__(self, movie):
        if isinstance(movie, Cinematheque):
            for m in movie:
                self.collection.append(m)
            self.stop += movie.stop
        elif isinstance(movie, Movie):
            self.collection.append(movie)
            self.stop += 1
        else:
            raise TypeError("Only Movies are allowed")
        return self

    def __sub__(self, movie):
        if isinstance(movie, Movie) and movie in self.collection:
            self.collection.remove(movie)
            self.stop -= 1
        else:
            raise TypeError("Only Movies are allowed")
        return self

    def __len__(self):
        return len(self.collection)

    def __bool__(self):
        if len(self.collection):
            return True
        return False


movies = Cinematheque()


def add_movie(title='', genre='', director=''):

    if not title:
        title = input("Enter the title of the movie: ")
    if not genre:
        genre = input("Enter the genre of the movie: ")
    if not director:
        director = input("Enter the director of the movie: ")
    year = input("Enter the year of the movie: ")
    if year_validation(year):
        movie = Movie(name=title, genre=genre, director=director, year=int(year))
        movies.append(movie)
    else:
        print('Be careful with entering a year!!!')
        return add_movie(title=title, genre=genre, director=director)


def list_movies():
    if movies:
        print(movies)
    else:
        print('There is no movies in your library yet')


def search():
    print("""Do you want to search by title? Press 1 than.
    Do you want to search by genre? Press 2 than. 
    Do you want to search by director? Press 3 than.
    Do you want to search by year? Press 4 than.
    Press 5 to Quit""")

    ans = input()
    if ans.lower() == 'q':
        exit()
    elif ans == '1':
        gener = search_by_title()
    elif ans == '2':
        gener = search_by_genre()
    elif ans == '3':
        gener = search_by_director()
    elif ans == '4':
        gener = search_by_year()
    else:
        return search()

    count = 0
    items = Cinematheque()
    for item in gener:
        items.append(item)
        count += 1

    if count == 0:
        print("There are no movie with given parameters in the collection.")
    else:
        for i in items:
            print(i)


def search_by_title():
    title = input('Enter a title: ')
    for movie in movies:
        if movie.name == title.lower():
            yield movie


def search_by_genre():
    genre = input('Enter a genre: ')
    for movie in movies:
        if movie.genre == genre.lower():
            yield movie


def search_by_director():
    director = input('Enter a director: ')
    for movie in movies:
        if movie.director == director.lower():
            yield movie


def search_by_year():
    year = input('Enter a year: ')
    year = year_validation(year)
    if not year:
        print("Be careful with entering a year!!!")
        return search_by_year()
    for movie in movies:
        if movie.year == year:
            yield movie
