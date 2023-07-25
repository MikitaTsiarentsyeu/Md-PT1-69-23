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

    words = text.split()
    chunks = []
    current_line_chunk = ''

    for word in words:
        if len(current_line_chunk) + len(word) + 1 <= max_chunk_size:
            current_line_chunk += word + ' '
        else:
            chunks.append(current_line_chunk.strip())
            current_line_chunk = word + ' '

    if current_line_chunk:
        chunks.append(current_line_chunk.strip())

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

    if len(chunk) >= max_chunk_size:
        return chunk

    words = chunk.split()
    num_words = len(words)
    num_spaces_needed = max_chunk_size - len(chunk) + num_words - 1
    num_spaces_between_words = num_spaces_needed // (
        num_words - 1) if num_words > 1 else 0
    extra_spaces = num_spaces_needed % (num_words - 1) if num_words > 1 else 0

    adjusted_chunk = words[0]

    for word in words[1:]:
        num_spaces = num_spaces_between_words + (1 if extra_spaces > 0 else 0)
        adjusted_chunk += ' ' * num_spaces + word
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

    output_file_path = OUTPUT_FILE_NAME

    try:
        with open(input_file_path, 'r') as input_file, \
                open(output_file_path, 'w') as output_file:
            for line in input_file:
                line = line.strip()
                chunks = split_text_into_chunks(line, max_chunk_size)

                for i, chunk in enumerate(chunks, 1):
                    if i < len(chunks):
                        adjusted_chunk = adjust_chunk_length(
                            chunk, max_chunk_size)
                        output_file.write(adjusted_chunk + '\n')
                    else:
                        output_file.write(chunk + '\n')

        print(f'File processing completed successfully.\n'
              f'Processed text saved in {output_file_path}.')

    except FileNotFoundError:
        print(f'Error: File {input_file_path} not found.')
    except Exception as e:
        print(f'An error occurred: {e}')


def main():
    """
    The main function that prompts the user for the maximum chunk size and
    initiates the text processing.
    """

    input_file_path = INPUT_FILE_NAME

    while True:
        try:
            max_chunk_size = int(input(
                'Enter the maximum number of characters per line\n'
                f'(should be greater than {MIN_CHUNK_SIZE}): '))
            if max_chunk_size <= MIN_CHUNK_SIZE:
                print(f'Error: The maximum chunk size should be greater'
                      f' than {MIN_CHUNK_SIZE}.')
            else:
                process_file(input_file_path, max_chunk_size)
                break
        except ValueError:
            print('Error: Please enter a valid integer for the '
                  'maximum chunk size.')
        except FileNotFoundError:
            print(f"Error: The file '{input_file_path}' not found. "
                  "Make sure the file is placed in the script's directory.")
        except Exception as e:
            print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
