"""
This script processes a text file, splits its lines into chunks, and adjusts
the chunk lengths to fit a maximum size.

Usage:
1. Place the input text file in the same directory as this script.
2. Run the script, and it will prompt you to enter the maximum number of
characters per line.
3. The script will process the text, split it into chunks, and save the result
in 'formatted_text.txt'.

Notes:
- The maximum chunk size should be greater than 35 characters for effective
formatting.
- The input text file should be provided with the name 'text.txt' in the
script's directory.
"""


MIN_CHUNK_SIZE = 35
OUTPUT_FILE_NAME = 'formatted_text.txt'
INPUT_FILE_NAME = 'text.txt'


def split_text_into_chunks(text, max_chunk_size):
    """
    Splits the given text into chunks of words, where each chunk has a length
    not exceeding the specified max_chunk_size.

    Args:
        text (str): The input text to be split into chunks.
        max_chunk_size (int): The maximum allowed number of characters per
        line.

    Returns:
        list: A list of chunks, each containing a subset of the input text.

    Example:
        >>> text = "This is a sample text that needs to be split into chunks."
        >>> max_size = 15
        >>> chunks = split_text_into_chunks(text, max_size)
        >>> chunks
        ['This is a', 'sample text', 'that needs to', 'be split into', 'chunks.']
    """

    # Split the input text into individual words (words are separated by
    # spaces, tabs, and newline characters).
    words = text.split()

    # List to store the resulting text "chunks."
    chunks = []

    # Variable to hold the current "chunk" of text being formed as we process
    #  words.
    current_line_chunk = ''

    # Iterate through each word in the text.
    for word in words:
        # Check if the current word fits within the current "chunk" of text,
        # considering spaces.
        if len(current_line_chunk) + len(word) + 1 <= max_chunk_size:
            # If the word fits, add it to the current "chunk" with a space.
            current_line_chunk += word + ' '
        else:
            # If the word doesn't fit, finish the current "chunk" of text and
            # add it to the chunks list.
            chunks.append(current_line_chunk.strip())
            # Then start a new "chunk" with the current word.
            current_line_chunk = word + ' '

    # Add the last "chunk" of text to the list if it remains unfinished.
    if current_line_chunk:
        chunks.append(current_line_chunk.strip())

    # Return the list of text "chunks."
    return chunks


def adjust_chunk_length(chunk, max_chunk_size):
    """
    Adjusts the length of a chunk by adding spaces to fit the specified
    max_chunk_size.

    Args:
        chunk (str): The chunk of text to be adjusted.
        max_chunk_size (int): The maximum allowed number of characters per
        line.

    Returns:
        str: The adjusted chunk with added spaces.

    Example:
        >>> chunk = "This is a sample"
        >>> max_size = 20
        >>> adjusted_chunk = adjust_chunk_length(chunk, max_size)
        >>> adjusted_chunk
        'This    is    a    sample'
    """

    # If the input chunk is already equal to or longer than the maximum size,
    # return it unchanged.
    if len(chunk) >= max_chunk_size:
        return chunk

    # Split the chunk into individual words.
    words = chunk.split()
    num_words = len(words)

    # Calculate the number of spaces needed to reach the maximum size.
    num_spaces_needed = max_chunk_size - len(chunk) + num_words - 1

    # Calculate the number of spaces to distribute between words.
    num_spaces_between_words = num_spaces_needed // (
        num_words - 1) if num_words > 1 else 0

    # Calculate any extra spaces that should be distributed between words.
    extra_spaces = num_spaces_needed % (num_words - 1) if num_words > 1 else 0

    # Create the adjusted chunk by adding spaces between words.
    adjusted_chunk = words[0]  # Start with the first word.

    # Iterate through the remaining words.
    for word in words[1:]:
        # Determine the number of spaces to add after the word.
        num_spaces = num_spaces_between_words + (1 if extra_spaces > 0 else 0)

        # Add the word and the calculated spaces to the adjusted chunk.
        adjusted_chunk += ' ' * num_spaces + word

        # Decrement the count of extra spaces if we used one for this word.
        extra_spaces = max(0, extra_spaces - 1)

    return adjusted_chunk


def process_file(input_file_path, max_chunk_size):
    """
    Processes the input file, splits each line into chunks, and saves the
    result in a new file 'formatted_text.txt'.

    Args:
        input_file_path (str): The path to the input text file.
        max_chunk_size (int): The maximum allowed number of characters per
        line.
    """


# Define the output file path to store the processed text.
    output_file_path = OUTPUT_FILE_NAME

    try:
        # Open the input file for reading and the output file for writing.
        with open(input_file_path, 'r') as input_file, \
                open(output_file_path, 'w') as output_file:
            # Process each line in the input file.
            for line in input_file:
                # Remove leading and trailing whitespaces from the line.
                line = line.strip()

                # Split the line into smaller chunks based on the specified
                # max_chunk_size.
                chunks = split_text_into_chunks(line, max_chunk_size)

                # Process each chunk.
                for i, chunk in enumerate(chunks, 1):
                    # If the chunk is not the last one, adjust its length to
                    # the maximum size.
                    if i < len(chunks):
                        adjusted_chunk = adjust_chunk_length(
                            chunk, max_chunk_size)
                        # Write the adjusted chunk to the output file,
                        # followed by a newline.
                        output_file.write(adjusted_chunk + '\n')
                    else:
                        # For the last chunk, write it to the output file as
                        # is, followed by a newline.
                        output_file.write(chunk + '\n')

        # Print a success message after processing the file.
        print(f'File processing completed successfully.\n'
              f'Processed text saved in {output_file_path}.')

    except FileNotFoundError:
        # Handle the case where the input file is not found.
        print(f'Error: File {input_file_path} not found.')

    except Exception as e:
        # Catch and handle any other exceptions that might occur during file
        # processing.
        print(f'An error occurred: {e}')


def main():
    """
    The main function that prompts the user for the maximum chunk size and
    initiates the text processing.
    """

    # Set the input file path to the name of the input file.
    input_file_path = INPUT_FILE_NAME

    while True:
        try:
            # Prompt the user to input the maximum number of characters per
            # line (max_chunk_size).
            max_chunk_size = int(input(
                'Enter the maximum number of characters per line\n'
                f'(should be greater than {MIN_CHUNK_SIZE}): '))

            # Check if the entered max_chunk_size is less than or equal to the
            # MIN_CHUNK_SIZE.
            if max_chunk_size <= MIN_CHUNK_SIZE:
                # Display an error message if the entered max_chunk_size is not
                # greater than MIN_CHUNK_SIZE.
                print(f'Error: The maximum chunk size should be greater'
                      f' than {MIN_CHUNK_SIZE}.')
            else:
                # If the max_chunk_size is valid, call the process_file
                # function to handle the file processing.
                process_file(input_file_path, max_chunk_size)

                # Break the while loop as the file processing is successful.
                break

        except ValueError:
            # Catch the ValueError when the user enters a non-integer value for
            # max_chunk_size.
            print('Error: Please enter a valid integer for the '
                  'maximum chunk size.')

        except FileNotFoundError:
            # Catch the FileNotFoundError when the specified input file is not
            # found.
            print(f"Error: The file '{input_file_path}' not found. "
                  "Make sure the file is placed in the script's directory.")

        except Exception as e:
            # Catch and handle any other exceptions that might occur during
            # file processing.
            print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
