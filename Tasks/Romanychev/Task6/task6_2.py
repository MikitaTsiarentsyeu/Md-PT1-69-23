import re
import requests
from bs4 import BeautifulSoup
from collections import defaultdict


# Clean and normalize the input text by removing non-alphanumeric characters
# and spaces, and converting it to lowercase.
def clean_and_normalize_text(text):
    """
    Clean and normalize the input text by removing non-alphanumeric characters
    and spaces, and converting it to lowercase.

    Args:
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

    Args:
        text (str): The text to be checked for a palindrome.

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

    Args:
        the_string (str): The input string to be checked for a palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_string = clean_and_normalize_text(the_string)
    return recursive_palindrome_check(cleaned_string)


def fetch_texts_from_url(url, element_name, start_index,
                         end_index, limit=None):
    """
    Fetch texts from a web page by URL and extract them from specific elements.

    Args:
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

    Args:
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

    urls = [
        # List of dictionaries with URL information to fetch texts from
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

    test_strings = [" ", 'A', '  ', '   ', 'Ток как кот']

    counters = defaultdict(int)
    categorized_strings = defaultdict(list)

    # Loop through URLs and fetch texts from web pages
    for url_info in urls:
        try:
            parsed_texts = fetch_texts_from_url(**url_info)
            test_strings.extend(parsed_texts)
        except ConnectionError as e:
            print(f"Failed to fetch the URL: {url_info['url']}. Error: {e}")

    # Iterate through test strings to categorize and count palindromes
    for text in test_strings:
        cleaned_text = clean_and_normalize_text(text)

        if is_string_palindrome(cleaned_text):
            counters['palindrome'] += 1
            if len(text) > 1 and text.strip() and " " in text and recursive_palindrome_check(text.lower()):
                counters['palindrome_with_spaces'] += 1
                categorized_strings['palindrome_with_spaces'].append(text)
            categorized_strings['palindrome'].append(text)
        else:
            counters['non_palindrome'] += 1
            categorized_strings['non_palindrome'].append(text)

    # Print the categorized strings with labels and their counts
    for category, count in counters.items():
        print_strings_with_label(categorized_strings[category],
                                 f"{category.capitalize()}s ({count}):")


if __name__ == "__main__":
    main()
