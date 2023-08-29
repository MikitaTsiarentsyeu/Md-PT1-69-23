import back_end

def start():
    while True:
        user_choice = input("""\nPlease, choose your action:
        Enter 1 if you want to look at the whole list of movies
        Enter 2 if you want to add a movie to the list
        Enter 3 if you want to search for a movie/movies
        Enter any other key if you want to quit the program\n""")

        if user_choice == "1":
            list_of_movies()
        elif user_choice == "2":
            add_movie()
        elif user_choice == "3":
            search_movie()
        else:
            print("Thank you! Bye!")
            break


def list_of_movies():
    whole_list = back_end.whole_list()
    print(f"The list of movies in the collection:\n\n{whole_list}")


def add_movie():
    new_movie = []

    for headline in back_end.headlines:
        user_info = input(f'Please, enter the {headline}\n')
        if headline == "year" and back_end.year_validation(user_info) == False:
            return print('The movie is not added to the collection')
        elif user_info == '':
            return print('You need to fill all of the description information')
        elif headline == "year" and back_end.year_validation(user_info) == True:
            new_movie.append(int(user_info))
        else:
            new_movie.append(user_info)

    result = back_end.add_movie(*new_movie)

    if result:
        return print("The movie is successfully added to the collection")
    else:
        return print("The movie is already in the collection")


def search_movie():

    user_search = input("""Please, choose the search option:
        Enter 1 if you want to search a movie/movies by title
        Enter 2 if you want to search a movie/movies by director
        Enter 3 if you want to search a movie/movies by release year
        Enter 4 if you want to search a movie/movies by genre
        Enter any other key if you want to quit the search\n""")

    list_of_options = ["1", "2", "3", "4"]
    for i, headline in enumerate(back_end.headlines, start = 1):
        if user_search not in list_of_options:
            print("The search is cancelled")
            break
        elif int(user_search) == i:
            title_input = input(f'Please, enter the {headline}:\n')

    if user_search == "3" and back_end.year_validation(title_input) == False:
        return
    else:
        result = back_end.movie_search(user_search, title_input)

    if result:
        output_result = '\n'.join(x for x in result)
        return print(f"These movies were found:\n{output_result}")
    else:
        return print("There are no movies under given parameters in the collection")

