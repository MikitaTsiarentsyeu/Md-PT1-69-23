import json

with open("movies.json", "r") as file:
    collection = json.load(file)
    movies = collection.values()

headlines = ["title", "director", "year", "genre"]


def whole_list():
    formatted_list = []
    for item in movies:
        values = list(item.values())
        movie_info = info_output(values)
        formatted_list.append(movie_info)
    return "\n".join([x for x in formatted_list])


def add_movie(*user_input):
    new_movie = {key:value for key, value in zip(headlines, user_input)}
    if new_movie in movies:
        return False
    else:
        collection[str(len(collection)+1)] = new_movie

        with open("movies.json", "w") as file:
            json.dump(collection, file)

        return True


def movie_search(search_parameter, user_input):

    if search_parameter == "1":
        search_generator = search_by_title(user_input)
    elif search_parameter == "2":
        search_generator = search_by_director(user_input)
    elif search_parameter == "3":
        search_generator = search_by_year(user_input)
    elif search_parameter == "4":
        search_generator = search_by_genre(user_input)

    count = 0
    result_list = []
    for item in search_generator:
        values = list(item.values())
        count += 1
        result_list.append(info_output(values))

    if count == 0:
        return False
    else:
        return result_list




def search_by_title(search_input):
    for item in movies:
        if search_input.lower() == item["title"].lower():
            yield item


def search_by_director(search_input):
    for item in movies:
        if search_input.lower() == item["director"].lower():
            yield item


def search_by_year(search_input):
    search_input = int(search_input)
    for item in movies:
        if search_input == item["year"]:
            yield item


def search_by_genre(search_input):
    for item in movies:
        if search_input.lower() == item["genre"].lower():
            yield item


def year_validation(year_input):
    if len(year_input) != 4:
        print('The "year" value must contain 4 digits')
        return False

    try:
        int(year_input)
        return True
    except ValueError:
        print('The "year" value must be a number')
        return False


def info_output(movie_info_list):
    return f'"{movie_info_list[0]}" by {movie_info_list[1]}, {movie_info_list[2]}, ({movie_info_list[3]})'

