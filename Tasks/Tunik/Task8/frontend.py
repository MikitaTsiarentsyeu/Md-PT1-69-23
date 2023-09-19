import backend

def start():
    while True:
        menu = input("""Choose a point of menu:
            0.exit
            1.show all movies
            2.add a movie
            3.search by title
            4.search by director
            5.search by year
            6.search by genre\n""")
        if menu == '1':
            show_all()
        elif menu == '0':
            print("Have a good time!")
            break
        elif menu == '2':
            add_movie()
        elif menu == '3':
            search_by_title()
        elif menu == '4':
            search_by_director()
        elif menu == '5':
            search_by_year()
        elif menu == '6':
            search_by_genre()


def show_all():
    res = backend.show_all()
    print(res)

def add_movie():
    values = []
    for header in backend.headers:
        value = enter_value_by_key(header)
        values.append(value)
    res = backend.add_movie(*values)
    if res:
        print("the movie was added")
    else:
        print("the movie name is alredy in use")

def search_by_title():
    title = input("please enter the title: ")
    data_for_search = backend.search_by_title(title)
    i = 0
    if data_for_search:
        for item in data_for_search:
            print (item)
            i +=1
    if i <= 0:
        print("Sorry, nothing found ")

def search_by_director():
    director = input("please enter the director: ")
    data_for_search = backend.search_by_director(director)
    i = 0
    if data_for_search:
        for item in data_for_search:
            print (item)
            i +=1
    if i <= 0:
        print("Sorry, nothing found ")

def search_by_year():
    year = input("please enter the year: ")
    data_for_search = backend.search_by_year(year)
    i = 0
    if data_for_search:
        for item in data_for_search:
            print (item)
            i +=1
    if i <= 0:
        print("Sorry, nothing found ")

def search_by_genre():
    genre = input("please enter the genre: ")
    data_for_search = backend.search_by_genre(genre)
    i = 0
    if data_for_search:
        for item in data_for_search:
            print (item)
            i +=1
    if i <= 0:
        print("Sorry, nothing found ")

def enter_value_by_key(key):
    return input(f"please enter the movie {key}\n")