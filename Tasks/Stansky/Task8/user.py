import backend


def start():
    while True:
        choice = input("""choose a point of menu:
                0. Exit from program
                1. Show all films
                2. Add a film
                3. Remove a Film
                4. Search\n""")
        if choice == "1":
            show_all()
        elif choice == "0":
            print('Goodbye!')
            break
        elif choice == "2":
            add_product()
        elif choice == '3':
            remove_product()
        elif choice == '4':
            search()
        elif int(choice) > 4 or int(choice) < 0:
            print("Incorrect input, try again, please!")


def show_all():
    result = backend.show_all()
    print(result)


def add_product():
    values = []
    for atr in backend.attrs:
        value = enter_value(atr)
        values.append(value)
    result = backend.add_product(*values)
    if result:
        print("The Film was added")
        exit()
    else:
        print("The Film name already in use")


def remove_product():
    value = enter_value(backend.attrs[0])
    result = backend.remove_product(value)
    if result:
        print("The film was removed")
        exit()
    else:
        print("The film was not found")


def search():
    while True:
        choice_cat = input("""Please, choose a category to search for a film:
                   0. Title
                   1. Director
                   2. Year
                   3. Genre
                   4. Exit from program\n""")

        if choice_cat == '4':
            print("Goodbye!")
            break
        if int(choice_cat) < 0 or int(choice_cat) > 4 :
            print("Incorrect input")
            break

        text = input("Please, input text to search:\n")
        text = text.lower()
        category = backend.attrs[int(choice_cat)]
        search_res = backend.search(category, text)
        bank_result = 0
        print("Found according to your request:\n")
        if search_res:
            for item in search_res:
                print(item)
                bank_result += 1
        if not bank_result:
            print("Sorry, nothing found ")
            break


def enter_value(key):
    return input(f"Please, enter film {key}:\n")





