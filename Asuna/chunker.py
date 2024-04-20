class Chunker:
    def chunk(input_list, chunk_size: int):
        """
        Chunk a list into smaller sublists of the specified length.

        :param input_list: The list to be chunked.
        :param chunk_size: The length of each chunk.
        :return: A list of chunks.
        """
        if chunk_size <= 0:
            raise ValueError("Chunk size must be a positive integer.")

        return [input_list[x:x+chunk_size] for x in range(0, len(input_list), chunk_size)]

    def multi_chunk(*lists, chunk_size: int, default_value=None):
        """
        Chunk multiple lists by extracting one item from each list and forming sets.
        If a list runs out of items, use the default_value to fill in.

        :param lists: Multiple input lists.
        :param chunk_size: The length of each chunk.
        :param default_value: The value to use for lists that run out of items.
        :return: A list of chunks.
        """
        if chunk_size <= 0:
            raise ValueError("Chunk size must be a positive integer.")

        chunks = []
        num_lists = len(lists)

        for i in range(0, len(lists[0]), chunk_size):
            chunk = []

            for j in range(num_lists):
                if i < len(lists[j]):
                    chunk.append(lists[j][i])
                else:
                    chunk.append(default_value)

            chunks.append(chunk)

        return chunks
    

    def split(input_list, split_into: int):
        """
        Split a list into smaller sublists as evenly as possible.

        :param input_list: The list to be split.
        :param split_into: The number of sublists to split the list into.
        :return: A list of sublists.
        """
        if split_into <= 0:
            raise ValueError("Split into value must be a positive integer.")

        num_items = len(input_list)
        quotient, remainder = divmod(num_items, split_into)
        result = [input_list[i * quotient + min(i, remainder):(i + 1) * quotient + min(i + 1, remainder)] for i in range(min(split_into, num_items))]
        return result