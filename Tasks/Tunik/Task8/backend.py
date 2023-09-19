import json 

with open("data.json","r") as file:
    base = json.load(file)
    data = base.values()
    headers = ["title","director","year","genre"]



def show_all():
   return  '\n'.join([format_data(x) for x in data])

def add_movie(*values):
    new_movie = {key:value for key, value in zip(headers,values)}
    if new_movie in data:
        return False
    else:
        base[str(len(base)+1)] = new_movie
    with open("data.json","w") as file:
        json.dump(base,file)
    file.close()
    return True

def search_by_title(title):
    for movie in data:
        if title.lower() == movie["title"].lower():
            yield movie

def search_by_director(director):
    for movie in data:
        if director.lower() == movie["director"].lower():
            yield movie

def search_by_year(year):
    year = int(year)
    for movie in data:
        if year == movie["year"]:
            yield movie

def search_by_genre(genre):
    for movie in data:
        if genre.lower() == movie["genre"].lower():
            yield movie        

def format_data(data):
    return ';'.join([f"{k}:{v}" for k, v in data.items()])
   


