import json


with open("anime_series.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

fields = ["title", "studios", "year", "genres"]


def greeting_message():
    return "Welcome to digital anime series storage!"


def goodbye_message():
    return "Thank you for using our storage, have a great day!"


def action():
    return input("Your choice: ")


def all_anime_series():
    result = []
    for pos, series in data.items():
        element = ""
        element = f"{element}{pos}. "
        lines = '\n'.join(line for line in format_anime_series(series))
        element = f"{element}{lines}"
        result.append(element)
    return result


def format_anime_series(anime_series):
    result = []
    for key, value in anime_series.items():
        line = ""
        if key == "title":
            line = f"{line}{value}"
        elif key == "genres":
            line = f"{line}{key}: {', '.join(genre for genre in value)}"
        else:
            line = f"{line}{key}: {value}"
        result.append(line)
    return result


def filling_new_series(new_title):
    new_series = [new_title]
    for field in fields[1:]:
        value = input(f"{field} - ")
        if field == "year":
            new_series.append(int(value))
        elif field == "genres":
            new_series.append(value.split(", "))
        else:
            new_series.append(value)
    return {field: value for field, value in zip(fields, new_series)}


def add_new_anime_series(new_series):
    new_pos = int(list(data.keys())[-1])+1
    data[str(new_pos)] = new_series
    with open("anime_series.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)


def search_by_title(title_seek):
    for anime_series in data.values():
        if anime_series["title"] == title_seek:
            yield anime_series


def search_by_studios(studios_seek):
    for anime_series in data.values():
        if anime_series["studios"] == studios_seek:
            yield anime_series


def search_by_year(year_seek):
    for anime_series in data.values():
        if anime_series["year"] == year_seek:
            yield anime_series


def search_by_genre(genre_seek):
    for anime_series in data.values():
        for genre in anime_series["genres"]:
            if genre == genre_seek:
                yield anime_series
                break
