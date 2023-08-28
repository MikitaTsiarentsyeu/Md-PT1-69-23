import tabulate #printing small tables without hassle
from back import DataBase as db

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
                db.post_collection(dict)
            elif number == 2:
                db.get_collection(list)
            elif number == 4:
                print('\nBye, all the best!')
                exit()
            elif number == 3:
                search = input('\nI am a smart search and I can search by: \n1) by Title picture\n2) by Author picture\n'
                               '3) by Year picture\n4) by Genre picture''\n\nEnter the search number you are interested in: ')
                try:
                    search = int(search)
                    if search not in [1, 2, 3, 4]:
                        raise RuntimeError("\nYou entered not an integer or there is no such menu item, try again: ")
                    elif search == 1:
                        title = input('Enter the Title of the picture: ')
                        print(tabulate.tabulate([x for x in db.gen_search_in_collection(title, 'title')], showindex="always"))
                    elif search == 2:
                        author = input('Enter the Author of the picture: ')
                        print(tabulate.tabulate([x for x in db.gen_search_in_collection(author, 'author')], showindex="always"))
                    elif search == 3:
                        year = input('Enter the Year of the picture: ')
                        print(tabulate.tabulate([x for x in db.gen_search_in_collection(year, 'year')], showindex="always"))
                    elif search == 4:
                        genre = input('Enter the Genre of the picture: ')
                        print(tabulate.tabulate([x for x in db.gen_search_in_collection(genre, 'genre')], showindex="always"))
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


