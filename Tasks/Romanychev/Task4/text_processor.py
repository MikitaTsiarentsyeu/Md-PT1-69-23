class TextProcessor:
    def __init__(self, max_chunk_size):
        self.max_chunk_size = max_chunk_size

    def split_text_into_chunks(self, text):
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
