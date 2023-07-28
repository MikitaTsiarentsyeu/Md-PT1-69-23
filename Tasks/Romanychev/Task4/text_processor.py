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
    'This is a sample'
    Note:
     - If  the input chunk is already equal to or longer than the maximum size,
    it is returned unchanged.
     - The  function  adds  spaces  between  words  in  the chunk to adjust its
    length, maintaining proper spacing.
     - The extra spaces are distributed evenly between words, starting from the
    leftmost word.
     - The final adjusted chunk is returned as the result.
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
