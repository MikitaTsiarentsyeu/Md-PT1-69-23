def split_text_into_chunks(text, max_chunk_size):
    """
    Splits the given text into chunks of words, where each chunk has a length
    not exceeding the specified max_chunk_size.
    Args:
    text (str): The input text to be split into chunks.
    max_chunk_size (int): The maximum allowed number of characters per line.
    Returns:
    list: A list of chunks, each containing a subset of the input text.
    Example:
      >>> text = "This is a sample text that needs to be split into chunks."
      >>> max_size = 15
      >>> chunks = split_text_into_chunks(text, max_size)
      >>> chunks
    ['This is a', 'sample text', 'that needs to', 'be split into', 'chunks.']
    Note:
     - The input text is split into individual words based on spaces, tabs, and
    newline characters.
     - The  function  forms  chunks of words in such a way that each chunk does
    not exceed the max_chunk_size.
     - Trailing  spaces  are  removed  from  each chunk before adding it to the
    result list.
    """

    # Split the input text into individual words (words are separated by
    # spaces, tabs, and newline characters).
    words = text.split()

    # List to store the resulting text "chunks."
    chunks = []

    # Variable to hold the current "chunk" of text being formed as we process
    # words.
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
    Adjusts  the length of a given chunk of text by distributing spaces between
    words.
    If the input chunk is already equal to or longer than the maximum size,
    it will be returned unchanged.
    Args:
    chunk (str): The input chunk of text to be adjusted.
    max_chunk_size (int): The maximum desired size of the adjusted chunk.
    Returns:
    str: The adjusted chunk of text with spaces distributed between words.
    """

    # If the input chunk is already equal to or longer than the maximum size,
    # return it unchanged.
    if len(chunk) >= max_chunk_size:
        return chunk

    # Split the chunk into individual words.
    words = chunk.split()

    # Calculate the total number of spaces needed to achieve the desired chunk
    # size
    total_spaces = max_chunk_size - sum(map(len, words))

    # Calculate the number of spaces to distribute between words
    num_words = len(words)
    spaces_per_word, extra_spaces = divmod(total_spaces, num_words - 1)

    # Generate the list with the distributed spaces using a list comprehension
    space_counts = [spaces_per_word + (1 if index < extra_spaces else 0)
                    for index in range(num_words - 1)]

    # Add 0 at the end of the space_counts list
    space_counts.append(0)

    # Combine words with their corresponding space counts using a list
    # comprehension
    words_with_spaces = [word + ' ' * spaces_to_add for word,
                         spaces_to_add in zip(words, space_counts)]

    # Join the words with spaces using the str.join method
    adjusted_chunk = words_with_spaces[0] + ''.join(words_with_spaces[1:])

    return adjusted_chunk
