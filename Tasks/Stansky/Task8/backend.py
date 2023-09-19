import json

with open("warbros_films.json", "r") as f:
    inf = json.load(f)
*bank, = inf.values()
attrs = ["Title", "Director", "Year", "Genre"]


def show_all():
    return '\n'.join([format_product(x) for x in bank])


def add_product(*values):
    for product in bank:
        if product["Title"] == values[0]:
            return False
    product = {atr: value for atr, value in zip(attrs, values)}
    new_key = int(list(inf.keys())[-1])+1
    inf[new_key] = product
    with open("warbros_films.json", "w") as file:
        json.dump(inf, file, indent=4)
    return True


def remove_product(title):
    for i,  product in enumerate(bank):
        if product["Title"].lower() == title.lower():
            del inf[str(i+1)]
            with open("warbros_films.json", "w") as file:
                json.dump(inf, file, indent=4)
            return True
    return False


def search(category, text):

    if category == "Title":
        return search_by_title(text)
    if category == "Director":
        return search_by_director(text)
    if category == "Year":
        return search_by_year(int(text))
    if category == "Genre":
        return search_by_genre(text)


def search_by_title(text):
    for res in inf.values():
        bank_search = res["Title"].lower()
        if text in bank_search:
            yield res


def search_by_director(text):
    for res in inf.values():
        bank_search = res["Director"].lower()
        if text in bank_search:
            yield res


def search_by_year(text):
    for res in inf.values():
        bank_search = res["Year"]
        if str(text) in str(bank_search):
            yield res


def search_by_genre(text):
    for res in inf.values():
        bank_search = res["Genre"].lower()
        if text in bank_search:
            yield res


def format_product(product):
    return ';'.join([f"{k}:{v}" for k, v in product.items()])



