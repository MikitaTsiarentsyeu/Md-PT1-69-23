from back_end import Collection

def main():
    collection = Collection('data.json')
    while True:
        print("Select an option:")
        print("1. Add a new album or movie to the collection")
        print("2. List all albums or movies in the collection")
        print("3. Search for an album or movie by title")
        print("4. Search for an album or movie by artist/director")
        print("5. Search for an album or movie by year")
        print("6. Search for an album or movie by genre")
        print("7. Quit the program")

        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            title = input("Enter the title: ")
            artist_or_director = input("Enter the artist or director: ")
            year = input("Enter the year: ")
            genre = input("Enter the genre: ")
            collection.add_item(title, artist_or_director, year, genre)
            print("Item added to collection.")
        elif choice == '2':
            items = collection.list_items()
            if not items:
                print("No items in collection.")
            else:
                for item in items:
                    print(f"{item['title']} ({item['year']}) by {item['artist_or_director']} ({item['genre']})")
        elif choice == '3':
            search_term = input("Enter the title to search for: ")
            results = collection.search_by_title(search_term)
            print_results(results)
        elif choice == '4':
            search_term = input("Enter the artist/director to search for: ")
            results = collection.search_by_artist(search_term)
            print_results(results)
        elif choice == '5':
            search_term = input("Enter the year to search for: ")
            results = collection.search_by_year(search_term)
            print_results(results)
        elif choice == '6':
            search_term = input("Enter the genre to search for: ")
            results = collection.search_by_genre(search_term)
            print_results(results)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def print_results(results):
    count = 0
    for item in results:
        count += 1
        print(f"{count}. {item['title']} ({item['year']}) by {item['artist_or_director']} ({item['genre']})")
    if count == 0:
        print("No results found.")

if __name__ == '__main__':
    main()