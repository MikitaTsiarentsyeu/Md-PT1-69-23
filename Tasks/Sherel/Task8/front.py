import tabulate #printing small tables without hassle
from back import DataBase

db = DataBase('data.json')

def main():
    while True:
        number = input(f"""\nThe most famous paintings in the world
1) Add a new artwork to the collection.
2) List all artwork in the collection.
3) Search for an artwork by title, author, year, or genre.
4) Quit the program.

Please select the desired action: """)
        try:
            number = int(number)
            if number not in [0, 1, 2, 3, 4]:
                raise RuntimeError("\nYou entered not an integer or there is no such menu item, try again: ")
            elif number == 0:
                main()
            elif number == 1:
                message_for_user = ["Name picture: ", "Author picture: ", "Year picture: ", "Genre picture: "]
                headers = ["title", "author", "year", "genre"]
                user_inputs = []
                for x in message_for_user:
                    while True:
                        input_value = input(x)
                        if not input_value:
                            print("The field cannot be empty, please enter a value.")
                        else:
                            user_inputs.append(input_value)
                            break
                print('\nThe picture has been added to the database.') if db.post_collection(headers, user_inputs) is True else print('oops')
            elif number == 2:
                print('\nDatabase is empty or missing') if db.get_collection() == None else (
                    print(f'\n{tabulate.tabulate(db.get_collection(), headers="firstrow")}'))
            elif number == 4:
                print('\nBye, all the best!')
                exit()
            elif number == 3:
                search = input('\nI am a smart search and I can search by: \n1) by Title picture\n2) by Author picture\n'
                               '3) by Year picture\n4) by Genre picture''\n\nEnter the search number you are interested in: ')
                try:
                    test = {'1': 'title', '2': 'author', '3': 'year', '4': 'genre'}
                    for i in test:
                        if search in i:
                            search_input = input(f'Enter the {test[i]} of the picture: ')
                            print(f"""{tabulate.tabulate([x for x in db.gen_search_in_collection(search_input, test[i])])}""")
                except ValueError:
                    print("\nYou entered not an integer or there is no such menu item, try again: ")
        except ValueError:
            print("\nYou entered not an integer or there is no such menu item, try again: ")
        except RuntimeError as e:
             print(e)
        else:
            if input('\nBack main menu - send 0. Exit from program - send all value: ') == str(0):
                main()
            else:
                print('\nBye, all the best!')
                exit()

if __name__ == '__main__':
    main()