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
    while True:
        new_series = [new_title]
        print("Fill the next parameters of this series:")
        try:
            for field in fields[1:]:
                value = input(f"{field} - ")
                if field == "year":
                    new_series.append(int(value))
                elif field == "genres":
                    new_series.append(value.split(", "))
                else:
                    new_series.append(value)
            return {field: value for field, value in zip(fields, new_series)}
        except ValueError:
            print("Wrong info for this field, error happened, try again")


def add_new_anime_series(new_title):
    new_series = filling_new_series(new_title)
    new_pos = int(list(data.keys())[-1])+1
    data[str(new_pos)] = new_series
    with open("anime_series.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)


def search_anime_series():
    while True:
        try:
            print("""Choose field to search anime series from:

                1. Title
                2. Studios
                3. Year
                4. Genre

                5. Cancel the search""", end="\n\n")
            search_field = int(input("Your choice: "))
            print(f"\nWrite the {fields[search_field-1]} you're searching for:", end=" ")
            if search_field == 1:
                res = search_by_title(input())
            elif search_field == 2:
                res = search_by_studios(input())
            elif search_field == 3:
                res = search_by_year(input())
            elif search_field == 4:
                res = search_by_genre(input())
            elif search_field == 5:
                break
            else:
                raise ValueError
            print("\nThe following anime series were found: \n")
            order = 1
            for item in res:
                print(f"{order}.", end=" ")
                format_anime_series(item)
                order += 1
                print()
            if order == 1:
                print("No search results")
            break
        except ValueError:
            print("Wrong input")


def search_by_title(title_seek):
    for anime_series in data.values():
        if anime_series["title"] == title_seek:
            yield anime_series


def search_by_studios():
    pass


def search_by_year():
    pass


def search_by_genre():
    pass
