from random import shuffle
from functools import reduce

class List(list):
    def __init__(self, *args):
        """
        Initialize the List object.

        :param args: One or more lists to initialize the object with.
        """
        if len(args) == 1 and isinstance(args[0], list):
            super().__init__(args[0])
        else:
            super().__init__(*args)

    def split(self, split_into: int):
        """
        Split the list into smaller sublists as evenly as possible.

        :param split_into: The number of sublists to split the list into.
        :return: A list of sublists.
        """
        if split_into <= 0:
            raise ValueError("Split into value must be a positive integer.")

        num_items = len(self)
        quotient, remainder = divmod(num_items, split_into)
        result = [self[i * quotient + min(i, remainder):(i + 1) * quotient + min(i + 1, remainder)] for i in range(min(split_into, num_items))]
        return result

    def chunk(self, chunk_size: int):
        """
        Chunk the list into smaller sublists of the specified length.

        :param chunk_size: The length of each chunk.
        :return: A list of chunks.
        """
        if chunk_size <= 0:
            raise ValueError("Chunk size must be a positive integer.")

        return [self[x:x+chunk_size] for x in range(0, len(self), chunk_size)]
    
    def unique(self, keep_order=False):
        """
        Return a list with only unique elements, removing duplicates.

        :param keep_order: Whether to keep the order of elements or not.
        :return: A list with unique elements.
        """
        if keep_order:
            seen = []
            return [x for x in self if x not in seen and not seen.append(x)]
        else:
            return list(set(self))

    def shuffle(self):
        """
        Shuffle the elements of the list randomly.
        """
        shuffle(self)

    def flatten(self):
        """
        Flatten nested lists into a single-level list.

        :return: A flattened list.
        """
        def _flatten(lst):
            for el in lst:
                if isinstance(el, list):
                    yield from _flatten(el)
                else:
                    yield el

        return list(_flatten(self))

    def map(self, func):
        """
        Apply a function to each element of the list.

        :param func: The function to apply.
        :return: A new list with the function applied to each element.
        """
        return [func(x) for x in self]
    
    def filter(self, func):
        """
        Filter elements based on a condition.

        :param func: The filtering function.
        :return: A new list with elements that satisfy the condition.
        """
        return [x for x in self if func(x)]
    
    def reduce(self, func, initializer=None):
        """
        Reduce the list to a single value.

        :param func: The reducing function.
        :param initializer: The initial value for reduction.
        :return: The reduced value.
        """
        return reduce(func, self, initializer)
    
    def search_and_replace(self, search_value, replace_value):
        """
        Search for specific elements and replace them with another value.

        :param search_value: The value to search for.
        :param replace_value: The value to replace the searched value with.
        """
        for i, val in enumerate(self):
            if val == search_value:
                self[i] = replace_value

    def merge(self, *lists):
        """
        Merge multiple lists into one list.

        :param lists: Lists to merge with the current list.
        :return: A new list containing all elements from the current list and other lists.
        """
        merged_list = list(self)
        for lst in lists:
            merged_list.extend(lst)
        return merged_list
    
    def statistics(self):
        """
        Calculate basic statistics for the list.

        :return: A dictionary containing statistics such as mean, median, mode, variance, and standard deviation.
        """
        import statistics
        stats = {}
        stats['mean'] = statistics.mean(self)
        stats['median'] = statistics.median(self)
        stats['mode'] = statistics.mode(self)
        stats['variance'] = statistics.variance(self)
        stats['stdev'] = statistics.stdev(self)
        return stats

    def serialize_to_json(self, filename):
        """
        Serialize the list to JSON format and save it to a file.

        :param filename: The name of the file to save the JSON data to.
        """
        import json
        with open(filename, 'w') as f:
            json.dump(self, f)

    def serialize_to_csv(self, filename):
        """
        Serialize the list to CSV format and save it to a file.

        :param filename: The name of the file to save the CSV data to.
        """
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self)

    def deserialize_from_json(self, filename):
        """
        Deserialize the list from JSON format.

        :param filename: The name of the file containing the JSON data.
        """
        import json
        with open(filename, 'r') as f:
            data = json.load(f)
            self.extend(data)

    def deserialize_from_csv(self, filename):
        """
        Deserialize the list from CSV format.

        :param filename: The name of the file containing the CSV data.
        """
        import csv
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.extend(row)