import back

def start():
    while True:
        ch = input("""Make a choise:
                   1: exit
                   2. show all
                   3. add to collection
                   4. search by title
                   5. search by studios
                   6. search by year
                   7. search by genre \n""")
        if ch == '1':
            print('See ya')
            break
        elif ch == '2':
            show_all()
        elif ch == '3':
            add_movie()
        elif ch == '4':
            search_by_title()
        elif ch == '5':
            search_by_studios()
        elif ch == '6':
            search_by_year()
        elif ch == '7':
            search_by_genre()

def show_all():
    res = back.show_all()
    print(res)

def add_movie():
    values = []
    for header in back.headers:
        value = enter_value_by_key(header)
        values.append(value)
    res = back.add_movie(*values)
    if res:
        print("the movie was added")
    else:
        print("the movie name is alredy in use")

def search_by_title():
    title = input("please enter the title: ")
    data_for_search = back.search_by_title(title)
    i = 0
    if data_for_search:
        for item in data_for_search:
            print (item)
            i +=1
    if i <= 0:
        print("nothing found ")

def search_by_studios():
    studios = input("please enter a studio: ")
    data_for_search = back.search_by_studios(studios)
    i = 0
    if data_for_search:
        for item in data_for_search:
            print (item)
            i +=1
    if i <= 0:
        print("nothing found ")

def search_by_year():
    year = input("enter the year: ")
    data_for_search = back.search_by_year(year)
    i = 0
    if data_for_search:
        for item in data_for_search:
            print (item)
            i +=1
    if i <= 0:
        print("nothing found ")

def search_by_genre():
    genres = input("please enter the genre: ")
    data_for_search = back.search_by_genre(genres)
    i = 0
    if data_for_search:
        for item in data_for_search:
            print (item)
            i +=1
    if i <= 0:
        print("nothing found ")

def enter_value_by_key(key):
    return input(f"enter the movie {key}\n")