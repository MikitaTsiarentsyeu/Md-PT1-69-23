"""
Library System

This script provides a command-line interface for efficiently managing a
library system.
Users can perform various actions including listing items, adding new entries,
searching based on various criteria,
deleting items, and exiting the application.

The script interacts with a backend module to handle data storage and
retrieval.

Usage:
1. Run this script.
2. Follow the on-screen menu prompts to perform desired actions.

Usage Examples:
- To list all available items, select option 1 from the menu.
- To add a new item, choose option 2 and provide the required details.
- To find items by title, select option 3 and enter the title.
- For searching items by author, select option 4 and input the author's name.
- If searching items by year of release piques your interest, opt for option 5
and input the year.
- To search items by genre, select option 6 and enter the genre.
- To delete an item by its ID, select option 7 and input the corresponding ID.
- To gracefully conclude your interaction with the application, select
option 8.

"""

import backend  # Import the backend module for data handling

# Constants for menu choices
LIST_ITEMS_OPTION = '1'
ADD_ITEM_OPTION = '2'
SEARCH_TITLE_OPTION = '3'
SEARCH_AUTHOR_OPTION = '4'
SEARCH_YEAR_OPTION = '5'
SEARCH_GENRE_OPTION = '6'
DELETE_ITEM_OPTION = '7'
QUIT_OPTION = '8'


def add_item(data_store):
    """
    Add a new item to the library.

    Args:
        data_store (object): The data storage object from the backend module.

    Returns:
        None
    """
    # Collect input from the user
    prompts = [
        "Enter title: ",
        "Enter author: ",
        "Enter year: ",
        "Enter genre: "
    ]

    # Prompt the user for input for each field
    user_inputs = map(input, prompts)

    # Create a new item dictionary with incremental ID
    new_item = dict(zip(["title", "author", "year", "genre"], user_inputs))

    # Add the new item to the data store
    data_store.add_item(new_item)
    print("The item has been successfully added.")


def delete_item(data_store, item_id):
    """
    Delete an item from the library based on its ID.

    Args:
        data_store (object): The data storage object from the backend module.
        item_id (int): The ID of the item to be deleted.

    Returns:
        None
    """
    # Check if the item with the specified ID exists in the data store
    if data_store.delete_item_by_id(item_id):
        print("The item has been successfully deleted.")
    else:
        print("Sorry, the item with the specified ID was not found.")


def list_items(items):
    """
    Display a list of items in a tabular format.

    Args:
        items (list): List of item dictionaries to be displayed.

    Returns:
        None
    """
    items_list = list(items)
    if not items_list:
        print("No items found.")
        return

    # Define headers for the columns in the table
    headers = ["ID", "Title", "Author", "Year", "Genre"]

    # Calculate the appropriate column widths for formatting
    column_widths = {
        header: max(len(str(item[header.lower()])) for item in items_list)
        for header in headers
    }

    # Update the column widths to accommodate header lengths
    column_widths.update(
        {header: max(len(header), width)
         for header, width in column_widths.items()}
    )

    # Calculate the total width of the table
    total_width = sum(column_widths.values()) + len(headers) * 3 + 1
    horizontal_line = "-" * total_width

    # Format strings for the table header and data rows
    header_format = " | ".join(
        [f"{{:<{column_widths[header]}}}" for header in headers]
    )
    data_format = " | ".join(
        [f"{{:<{column_widths[header]}}}" for header in headers]
    )

    # Print the header row and horizontal line
    print(horizontal_line, header_format.format(
        *headers), horizontal_line, sep="\n")

    # Extract values for each item and print them in a formatted row
    item_values = map(
        lambda item: [item[header.lower()] for header in headers], items_list
    )
    for values in item_values:
        print(data_format.format(*values))

    # Print the horizontal line to complete the table
    print(horizontal_line)


def main():
    """
    Main function to run the Library System.

    Args:
        None

    Returns:
        None
    """
    # Create a data storage object using the backend module
    data_store = backend.create_data_store('data.json')

    # Define the menu options available to the user
    options = [
        "List all items",
        "Add a new item",
        "Search by title",
        "Search by author",
        "Search by year",
        "Search by genre",
        "Delete an item by ID",
        "Quit"
    ]

    # Main loop to repeatedly present the menu to the user
    while True:
        print(
            "\nWelcome to the Library System!\n\n\033[1;32mChoose an option:\033[0m")

        # Display the menu options with corresponding indices
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        # Get the user's choice from the menu
        choice = input("\n\033[1;32mEnter your choice: \033[0m")

        # Process the user's choice
        if choice == QUIT_OPTION:
            print("\n\033[1;32mUntil next time!\n"
                  "Remember, books open doors to new worlds.\n"
                  "Have a good day!\033[0m")

            break
        elif choice == LIST_ITEMS_OPTION:
            # Retrieve and display all items from the data store
            list_items(data_store.get_all_items())
        elif choice == ADD_ITEM_OPTION:
            # Add a new item to the data store
            add_item(data_store)
        elif choice == DELETE_ITEM_OPTION:
            # Prompt the user for an item ID and delete the item
            item_id = int(
                input("Please enter the ID of the item you want to delete: "))
            delete_item(data_store, item_id)
        elif choice in {SEARCH_TITLE_OPTION, SEARCH_AUTHOR_OPTION,
                        SEARCH_YEAR_OPTION, SEARCH_GENRE_OPTION}:
            # Prompt the user for a search term and display search results
            search_terms = {
                SEARCH_TITLE_OPTION: "title",
                SEARCH_AUTHOR_OPTION: "author",
                SEARCH_YEAR_OPTION: "year",
                SEARCH_GENRE_OPTION: "genre"
            }
            search_term = input(f"Enter {search_terms[choice]} to search: ")
            search_result = list(data_store.search_by_field(
                search_terms[choice], search_term))
            list_items(search_result)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
