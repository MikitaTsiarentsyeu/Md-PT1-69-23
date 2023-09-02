from backend import MovieCollection

def main():
    collection = MovieCollection('movies.json')
    collection.load_data()

    while True:
        print("\n Меню:")
        print("1. Добавить новый фильм")
        print("2. Список всех фильмов")
        print("3. Поиск по названию")
        print("4. Поиск по режиссеру")
        print("5. Поиск по году")
        print("6. Поиск по жанру")
        print("7. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            title = input("Введите название фильма: ")
            director = input("Введите режиссера фильма: ")
            year = input("Введите год выпуска: ")
            genre = input("Введите жанр: ")
            collection.add_movie(title, director, year, genre)
            print("Фильм успешно добавлен!")

        elif choice == '2':
            movies = collection.list_movies()
            for movie in movies:
                print(f"{movie['название']} ({movie['год']}), режиссер {movie['режиссер']}, жанр: {movie['жанр']}")

        elif choice == '3':
            search_term = input("Введите название для поиска: ")
            for movie in collection.search_by_title(search_term):
                print(f"{movie['название']} ({movie['год']}), режиссер {movie['режиссер']}")

        elif choice == '4':
            search_term = input("Введите режиссера для поиска: ")
            for movie in collection.search_by_director(search_term):
                print(f"{movie['название']} ({movie['год']}), режиссер {movie['режиссер']}")

        elif choice == '5':
            search_term = input("Введите год для поиска: ")
            for movie in collection.search_by_year(search_term):
                print(f"{movie['название']} ({movie['год']}), режиссер {movie['режиссер']}")

        elif choice == '6':
            search_term = input("Введите жанр для поиска: ")
            for movie in collection.search_by_genre(search_term):
                print(f"{movie['название']} ({movie['год']}), режиссер {movie['режиссер']}")

        elif choice == '7':
            print("До свидания!")
            break

if __name__ == "__main__":
    main()