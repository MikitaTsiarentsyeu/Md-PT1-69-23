import re
import requests
from bs4 import BeautifulSoup


def clean_and_normalize_text(text):
    """
    Clean and normalize the input text by removing non-alphanumeric characters
    and spaces, and converting it to lowercase.

    Parameters:
        text (str): The input text to be cleaned and normalized.

    Returns:
        str: The cleaned and normalized text.
    """

    cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', text)
    cleaned_text = cleaned_text.strip().lower()

    return cleaned_text


def recursive_palindrome_check(text):
    """
    Recursive helper function to check if the text is a palindrome.

    Parameters:
        text (str): The text to be checked for palindrome.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    text = re.sub(r'[^\w\s]', '', text)
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return recursive_palindrome_check(text[1:-1])


def is_string_palindrome(the_string):
    """
    Check if a given string is a palindrome.

    Parameters:
        the_string (str): The input string to be checked for palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_string = clean_and_normalize_text(the_string)
    return recursive_palindrome_check(cleaned_string)


def fetch_texts_from_url(url, element_name, start_index,
                         end_index, limit=None):
    """
    Fetch texts from a web page by URL and extract them from specific elements.

    Parameters:
        url (str): The URL of the web page to fetch texts from.
        element_name (str): The name of the HTML element to find and extract
        texts from.
        start_index (int): The starting index for slicing the elements.
        end_index (int): The ending index for slicing the elements.
        limit (int, optional): The maximum number of elements to fetch and
        process.

    Returns:
        list: A list of cleaned and normalized texts extracted from the
        specified elements.
    """
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all elements with the specified element_name
        all_elements = soup.find_all(element_name)

        if limit is not None:
            all_elements = all_elements[:limit]

        # Extract and return the text from the elements, excluding empty texts
        result = [element.text for element in
                  all_elements[start_index:end_index]
                  if element.text.strip()]
        return result

    else:
        raise ConnectionError(
            f"Failed to fetch the URL: {url}. Status code: "
            f"{response.status_code}")


def print_strings_with_label(strings, label):
    """
    Print a list of strings with a label.
    Parameters:
        strings (list): The list of strings to print.
        label (str): The label to print before the list.
    Returns:
        None
    """
    if strings:
        print(label + ":")
        for i, s in enumerate(strings, 1):
            print(
                f"{i}. '{s}' is {'' if is_string_palindrome(s) else 'not '}a palindrome")
    else:
        print(f"No {label.lower()} found.")


def main():
    print("Fetching texts from web pages...")

    # Define a list of dictionaries, each containing information about the URLs
    # to fetch texts from
    urls = [
        {
            'url': 'http://english2017.ru/english-palindrome',
            'element_name': 'span',
            'start_index': 7,
            'end_index': 57,
            'limit': None
        },
        {
            'url': 'https://www.analogi.net/igra/slova-palindromy-i-stroka-palindrom',
            'element_name': 'li',
            'start_index': 70,
            'end_index': 130,
            'limit': None
        },
    ]

    test_strings = [" ", 'A', '  ']
    for url_info in urls:
        url, element_name, start_index, end_index, limit = (
            url_info['url'],
            url_info['element_name'],
            url_info['start_index'],
            url_info['end_index'],
            url_info['limit']
        )

        try:
            parsed_texts = fetch_texts_from_url(
                url, element_name, start_index, end_index, limit)
            test_strings.extend(parsed_texts)
        except ConnectionError as e:
            print(f"Failed to fetch the URL: {url}. Error: {e}")

    # Use list comprehensions to categorize the test strings as palindromes
    # and non-palindromes
    palindromes = [text for text in test_strings if is_string_palindrome(text)]
    non_palindromes = [
        text for text in test_strings if not is_string_palindrome(text)
    ]
    palindrome_with_spaces = [
        text for text in test_strings if len(text) > 1 and text.strip() != "" and recursive_palindrome_check(text)
    ]

    # Print the palindromes and non-palindromes
    print_strings_with_label(palindromes, "Palindromes")
    print_strings_with_label(non_palindromes, "Non-Palindromes")
    print_strings_with_label(palindrome_with_spaces, "Palindromes with spaces")


if __name__ == "__main__":
    main()
