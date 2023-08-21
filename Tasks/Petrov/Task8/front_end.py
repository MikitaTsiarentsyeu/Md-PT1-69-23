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

        if action == "":
            break
        elif action == "1":
            pass  # todo
