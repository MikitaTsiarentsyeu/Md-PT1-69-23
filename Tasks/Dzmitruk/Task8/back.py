
collection = []

def add_to_collection():
    album = {}
    album["title"] = str(input("Please, enter the title of the album: "))
    album["artist"] = str(input("Please, enter the album artist: "))
    album["year"] = str(input("Please, enter the album year: "))
    while year_validation(album["year"]) == False:
        album["year"] = str(input("Please, enter the album year: "))
    album["genre"] = str(input("Please, enter the album genre: "))
    collection.append(album)
        
    return collection

def list_all_albums():
    for album in collection:
        print()
        print(album["title"])
        for k, v in album.items():
            print(k + " : " + v)

def out_view(result_list):
    for album in result_list:
        print()
        print(album["title"])
        for k, v in album.items():
            print(k + " : " + v)

def album_search():
    search_by = str(input("Please, enter a search term (title, artist, year or genre: "))
    param = str(input("Please, enter a search value: "))

    if search_by == "title":
        search_generator = search_by_title(param)
    elif search_by == "artist":
        search_generator = search_by_artist(param)
    elif search_by == "year":
        search_generator = search_by_year(param)
    elif search_by == "genre":
        search_generator = search_by_genre(param)

    count = 0
    result_list = []
    for item in search_generator:
        result_list.append(item)
        count += 1

    if count == 0:
        return print("There are no album with given parameters in the collection.")
    else:
        return out_view(result_list)

    
def search_by_title(param):
    for item in collection:
        if param.lower() == item["title"].lower():
            yield item


def search_by_artist(param):
    for item in collection:
        if param.lower() == item["artist"].lower():
            yield item


def search_by_year(param):
    for item in collection:
        if param == item["year"]:
            yield item


def search_by_genre(param):
    for item in collection:
        if param.lower() == item["genre"].lower():
            yield item


def year_validation(year):
    if len(year) != 4:
        print("The 'year' value must contain 4 digits.")
        return False

    try:
        int(year)
        return True
    except ValueError:
        print("The 'year' value must be a number.")
        return False