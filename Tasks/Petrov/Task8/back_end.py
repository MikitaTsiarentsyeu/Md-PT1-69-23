"""Module implements operation side for digital anime series storage"""

import json

FILE_PATH = "anime_series.json"

# Loading current storage database
with open(FILE_PATH, "r", encoding="UTF-8") as file:
    data = json.load(file)

fields = ["Title", "Studios", "Year", "Genres"]


def action():
    """Returns user input as option choice"""

    return input("Your choice: ")


def all_anime_series():
    """Returns list of strings of all anime series in storage"""

    result = []
    for pos, series in data.items():

        # Creating blank string for each element
        element = ""
        element = f"{element}{pos}. "
        lines = '\n'.join(line for line in format_anime_series(series))
        element = f"{element}{lines}"

        # Adding string interpretation of anime series in list
        result.append(element)
    return result


def format_anime_series(anime_series):
    """Returns list of strings with fields of one anime series"""

    result = []
    for key, value in anime_series.items():

        # Creating blank string for each field
        line = ""
        if key == "Title":
            line = f"{line}{value}"
        elif key == "Genres":
            line = f"{line}{key}: {', '.join(genre for genre in value)}"
        else:
            line = f"{line}{key}: {value}"

        # Adding string interpretation of field in list
        result.append(line)
    return result


def filling_new_series(new_title):
    """Returns dictionary object of new anime series

    new_title
        string for title of new anime series"""

    # Creating a list of all fields for new anime series
    new_series = [new_title]
    for field in fields[1:]:
        value = input(f"{field} - ")
        if field == "Year":
            new_series.append(int(value))
        elif field == "Genres":
            new_series.append(value.split(", "))
        else:
            new_series.append(value)
    return {field: value for field, value in zip(fields, new_series)}


def add_new_anime_series(new_series):
    """Adding new anime series to storage

    new_series
        new anime series as dictionary"""

    new_pos = int(list(data.keys())[-1])+1

    # Adding new anime series to local data dictionary
    data[str(new_pos)] = new_series

    with open(FILE_PATH, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)


def search_anime_series_by_field(field_seek, input_text):
    """Searching for anime series by field from inputted text.
    Returns generator with proper anime series

    field_seek
        string interpretation of searching field
    input_text
        inputted text as search line"""

    if field_seek == "Title":
        return search_by_title(input_text)
    if field_seek == "Studios":
        return search_by_studios(input_text)
    if field_seek == "Year":
        return search_by_year(int(input_text))
    if field_seek == "Genres":
        return search_by_genres(input_text.split(", "))


def search_by_title(title_seek):
    """Returns a generator that has anime series with proper title

    title_seek
        string line as search for title"""

    for anime_series in data.values():
        if anime_series["Title"].lower() == title_seek.lower():
            yield anime_series


def search_by_studios(studios_seek):
    """Returns a generator that has anime series with proper studios

    studios_seek
        string line as search for studios"""

    for anime_series in data.values():
        if anime_series["Ttudios"].lower() == studios_seek.lower():
            yield anime_series


def search_by_year(year_seek):
    """Returns a generator that has anime series with proper year

    year_seek
        integer as search for year"""

    for anime_series in data.values():
        if anime_series["Year"] == year_seek:
            yield anime_series


def search_by_genres(genres_seek):
    """Returns a generator that has anime series with proper genres

    genres_seek
        list of strings as search for genres"""

    for anime_series in data.values():
        set_seek = set([genre.lower() for genre in genres_seek])
        set_current = set([genre.lower() for genre in anime_series["Genres"]])
        if set_seek - set_current == set():
            yield anime_series
