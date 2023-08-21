import back_end


def welcome():
    back_end.greeting_message()
    back_end.separation()


def ending():
    back_end.separation()
    back_end.goodbye_message()


def process():
    while True:
        action = back_end.action()
        print()
        if action == "":
            break
        elif action == "1":
            back_end.list_all_anime_series()
        elif action == "2":
            back_end.add_new_anime_series()
        elif action == "3":
            back_end.search_anime_series()
        back_end.separation()
