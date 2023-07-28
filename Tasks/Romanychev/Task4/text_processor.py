class TextProcessor:
    """
    A  utility  class  for  processing  text  by  splitting  it into chunks and
    adjusting
    the length of each chunk to fit a specified maximum chunk size.
    Attributes:
    max_chunk_size (int): The maximum allowed number of characters per line.
    Methods:
    split_text_into_chunks(text):
    Splits the given text into chunks of words, where each chunk has a length
    not exceeding the specified max_chunk_size.
    adjust_chunk_length(chunk):
    Adjusts the length of a given chunk of text by distributing spaces between
    words. If the input chunk is already equal to or longer than the maximum
    size, it will be returned unchanged.
    """

    def __init__(self, max_chunk_size):
        """
        Initializes  a  new  instance  of  the  TextProcessor  class  with  the
        specified
        maximum chunk size.
        Args:
        max_chunk_size  (int):  The  maximum  allowed  number of characters per
        line.
        """

        self.max_chunk_size = max_chunk_size

    def split_text_into_chunks(self, text):
        """
        Splits  the  given  text  into  chunks of words, where each chunk has a
        length not exceeding the specified max_chunk_size.
        Args:
        text (str): The input text to be split into chunks.
        Returns:
        list: A list of chunks, each containing a subset of the input text.
        Example:
        >>> text = "This is a sample text that needs to be split into chunks."
        >>> max_size = 15
        >>> processor = TextProcessor(max_chunk_size=max_size)
        >>> chunks = processor.split_text_into_chunks(text)
        >>> chunks
        ['This  is  a',  'sample  text',  'that  needs  to',  'be  split into',
        'chunks.']
        Note:
        -  The input text is split into individual words based on spaces, tabs,
        and newline characters.
        -  The  function  forms  chunks  of words in such a way that each chunk
        does not exceed the max_chunk_size.
        -  Trailing  spaces are removed from each chunk before adding it to the
        result list.
        """

        words = text.split()
        chunks = []
        current_line_chunk = ''

        for word in words:
            if len(current_line_chunk) + len(word) + 1 <= self.max_chunk_size:
                current_line_chunk += word + ' '
            else:
                chunks.append(current_line_chunk.strip())
                current_line_chunk = word + ' '

        if current_line_chunk:
            chunks.append(current_line_chunk.strip())

        return chunks

    def adjust_chunk_length(self, chunk):
        """
        Adjusts  the  length  of  a  given chunk of text by distributing spaces
        between words.
        If  the  input  chunk  is  already  equal to or longer than the maximum
        size, it will
        be returned unchanged.
        Args:
        chunk (str): The input chunk of text to be adjusted.
        Returns:
        str: The adjusted chunk of text with spaces distributed between words.
        Example:
        >>> chunk = 'This is a'
        >>> max_size = 10
        >>> processor = TextProcessor(max_chunk_size=max_size)
        >>> adjusted_chunk = processor.adjust_chunk_length(chunk)
        >>> adjusted_chunk
        'This is a '
        """

        if len(chunk) >= self.max_chunk_size:
            return chunk

        words = chunk.split()
        total_spaces = self.max_chunk_size - sum(map(len, words))
        num_words = len(words)
        spaces_per_word, extra_spaces = divmod(total_spaces, num_words - 1)

        space_counts = [spaces_per_word + (1 if index < extra_spaces else 0)
                        for index in range(num_words - 1)]
        space_counts.append(0)

        words_with_spaces = [word + ' ' * spaces_to_add for word,
                             spaces_to_add in zip(words, space_counts)]
        adjusted_chunk = words_with_spaces[0] + ''.join(words_with_spaces[1:])

        return adjusted_chunk
