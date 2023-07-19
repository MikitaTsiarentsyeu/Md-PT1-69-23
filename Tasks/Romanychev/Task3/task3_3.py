import time
import re
import string
import matplotlib.pyplot as plt
from langdetect import detect_langs
from collections import Counter

# Function to detect the language of a given text


def detect_language(text):
    """
    Detects the language of the given text.

    Args:
        text (str): The input text to detect the language.

    Returns:
        tuple: A tuple containing the detected language code and a dictionary of
            language probabilities. The language code represents the detected
            language, and the dictionary contains the language codes as keys and
            their corresponding probabilities as values.
    """
    results = detect_langs(text)
    languages = {}
    for result in results:
        languages[result.lang] = result.prob
    language = max(languages, key=languages.get)
    return language, {language: languages[language]}


# Function to choose the source of the input string (keyboard or file)
def choose_source():
    source_choice = None
    while source_choice not in ['1', '2']:
        source_choice = input(
            "Choose the source of the string:\n1 - keyboard input,\n2 - file input.\nYour choice: ")
        if source_choice not in ['1', '2']:
            print("Invalid choice. Please select 1 or 2.")
    return source_choice


# Function to choose the language of the input string
def choose_language():
    language = None
    while language not in ['en', 'ru', 'pl', 'de', 'fr']:
        language = input(
            "Choose the language of the input string:\n'en' - English,\n'ru' - Russian,\n"
            "'pl' - Polish,\n'de' - German,\n'fr' - French.\nYour choice: ")
        if language not in ['en', 'ru', 'pl', 'de', 'fr']:
            print("Invalid choice. Please select from the provided languages.")
    return language


# Function to count the number of vowels in a string
def count_vowels(input_string, vowels):
    """
    Counts the number of vowels in a given string.

    Args:
        string (str): The input string.
        vowels (list): A list of vowels to count.

    Returns:
        dict: A dictionary containing the vowel counts, where the keys are the vowels and the values are the counts.
    """
    start_time = time.time()
    input_string_lower = input_string.lower()
    vowel_counts = {vowel: input_string_lower.count(vowel) for vowel in vowels}
    end_time = time.time()
    execution_time = end_time - start_time
    return vowel_counts, execution_time


# Function to count the occurrences of each word in a string
def count_words(input_string):
    """
    Counts the occurrences of each word in a given string, excluding punctuation and special characters.

    Args:
        input_string (str): The input string.

    Returns:
        dict: A dictionary containing the word counts, where the keys are the words and the values are the counts.
    """
    # Use regular expression to find all words in the text (excluding punctuation and special characters)
    words = re.findall(r'\b\w+\b', input_string.lower())
    word_counts = Counter(words)
    return word_counts


# Function to plot a histogram of vowel counts by language
def plot_histogram(vowel_counts_by_language):
    """
    Plots a histogram showing the distribution of vowel counts by language.

    Args:
        vowel_counts_by_language (dict): A dictionary containing the vowel counts for each language.
            The keys represent the language, and the values are dictionaries with vowel counts,
            where the keys are the vowels and the values are the counts.

    Returns:
        None
    """
    fig, ax = plt.subplots()

    for i, (language, vowel_counts) in enumerate(vowel_counts_by_language.items()):
        x = range(len(vowel_counts))
        height = list(vowel_counts.values())
        labels = list(vowel_counts.keys())

        ax.bar(x, height, align='center', label=language, color=plt.cm.Set3(i))

        for j, (h, l) in enumerate(zip(height, labels)):
            ax.text(j, h + 0.02 * max(height), str(h), ha='center')
            percentage = (h / sum(height)) * 100
            ax.text(j, h / 2, f"{percentage:.1f}%", ha='center', color='white')

    ax.set_xlabel('Vowel Characters')
    ax.set_ylabel('Count of Vowels')
    total_vowels = sum(vowel_counts.values())
    ax.set_title(
        f"COUNT OF VOWELS\n(text language - {''.join(language)})\ntotal number of vowels: {total_vowels}")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.yaxis.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    ax.legend()
    plt.xticks(x, labels)
    plt.show()


# Main program loop
while True:
    start_time = time.time()  # Start time of the program

    # Choose the source of the input string (keyboard or file)
    source_choice = choose_source()

    if source_choice == "1":
        # If keyboard input is chosen, prompt the user to choose the language and enter the string
        language = choose_language()
        user_input = input("Enter a string: ")
    else:
        try:
            # If file input is chosen, read the string from a file and detect its language

            # The language in the filename 'test(en)_task3_1.txt' can be changed to any language from the following list:
            # ['en', 'ru', 'pl', 'de', 'fr']

            with open('test(war and peace)_task3_1.txt', 'r') as file:
                user_input = file.read().strip()
            detected_language = detect_language(user_input)
            language = detected_language[0]
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred while reading the file:", str(e))

    # Define the vowels for each supported language
    vowels_by_language = {
        'en': ['a', 'e', 'i', 'o', 'u'],
        'ru': ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'],
        'pl': ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'],
        'de': ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü'],
        'fr': ['a', 'e', 'i', 'o', 'u']
    }

    # Count the number of vowels and words in the input string for the selected language
    vowel_counts_by_language = {}
    word_counts_by_language = {}

    vowel_counts, execution_time = count_vowels(
        user_input, vowels_by_language[language])

    word_counts = count_words(user_input)

    vowel_counts_by_language[language] = vowel_counts

    word_counts_by_language[language] = word_counts

    # Display the execution time for the specific function
    print(f"Execution time for 'count_vowels': {execution_time:.5f} seconds")

    # Plot a histogram of vowel counts by language
    # (the same as before, no changes needed)

    # Display the word counts for the input string
    print("\nWord counts for the input string:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

    # Count the number of unique words in the input string
    unique_word_count = len(word_counts)

    # Display the total number of unique words
    print(f"\nTotal number of unique words: {unique_word_count}")

    # Display the total execution time
    end_time = time.time()  # End time of the program
    total_execution_time = end_time - start_time  # Total execution time
    print(f"\nTotal execution time: {total_execution_time:.5f} seconds")

    # Prompt the user if they want to run the program again
    restart_choice = input("Do you want to run the program again? (y/n): ")
    while restart_choice.lower() not in ['y', 'n']:
        print("Invalid choice. Please enter 'y' or 'n'.")
        restart_choice = input("Do you want to run the program again? (y/n): ")

    if restart_choice.lower() == 'n':
        break  # Exit the loop if the user doesn't want to restart
