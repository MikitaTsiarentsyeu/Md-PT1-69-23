"""
The program allow the user 
to store and browse information about musical albums.
"""
import back

choice = None

while choice != "0":
    print(
        """
        1 - Add a new album to the collection.
        2 - List all albums in the collection.
        3 - Search for an album by title, artist, year, or genre.
        0 - Quit the program.
        """
        )
    choice = input("Enter a number: ")

    # exit
    if choice == "0":
        print("Goodbye.")
        exit()

    elif choice == "1":
        back.add_to_collection() 

    elif choice == "2":
        back.list_all_albums()

    elif choice == "3":
        back.album_search()
        
        # wrong input
    else:
        print("Sorry, your input is wrong.")