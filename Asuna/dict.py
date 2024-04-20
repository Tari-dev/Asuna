import json
import csv
from collections import defaultdict

class Dict(dict):
    def __init__(self, *args, **kwargs):
        """
        Initialize the Dict object.

        :param args: One or more dictionaries to initialize the object with.
        """
        super().__init__(*args, **kwargs)

    def default_value(self, default):
        """
        Set default values for missing keys.

        :param default: The default value to use for missing keys.
        """
        self.default = default

    def merge(self, *dicts):
        """
        Merge multiple dictionaries into one.

        :param dicts: Dictionaries to merge with the current dictionary.
        :return: A new dictionary containing all key-value pairs.
        """
        merged_dict = Dict(self)
        for d in dicts:
            merged_dict.update(d)
        return merged_dict

    def filter(self, func):
        """
        Filter keys and values based on a condition.

        :param func: The filtering function.
        :return: A new dictionary with filtered key-value pairs.
        """
        return Dict((k, v) for k, v in self.items() if func(k, v))

    def map_values(self, func):
        """
        Apply a function to all values in the dictionary.

        :param func: The function to apply.
        :return: A new dictionary with the function applied to all values.
        """
        return Dict((k, func(v)) for k, v in self.items())

    def flatten(self):
        """
        Flatten nested dictionaries into a single-level dictionary.

        :return: A flattened dictionary.
        """
        def _flatten(d, parent_key='', sep='_'):
            items = []
            for k, v in d.items():
                new_key = parent_key + sep + k if parent_key else k
                if isinstance(v, dict):
                    items.extend(_flatten(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, v))
            return dict(items)

        return Dict(_flatten(self))

    def reverse(self):
        """
        Reverse the keys and values in the dictionary.

        :return: A new dictionary with keys and values swapped.
        """
        return Dict((v, k) for k, v in self.items())

    def invert(self):
        """
        Invert the dictionary, swapping keys and values.

        :return: A new dictionary with keys and values inverted.
        """
        return Dict((v, k) for k, v in self.items())

    def sort_keys(self):
        """
        Sort the dictionary based on keys.

        :return: A new dictionary sorted by keys.
        """
        return Dict(sorted(self.items()))

    def sort_values(self):
        """
        Sort the dictionary based on values.

        :return: A new dictionary sorted by values.
        """
        return Dict(sorted(self.items(), key=lambda item: item[1]))

    def statistics(self):
        """
        Calculate basic statistics for values in the dictionary.

        :return: A dictionary containing statistics such as mean, median, mode, variance, and standard deviation.
        """
        import statistics
        stats = {}
        stats['mean'] = statistics.mean(self.values())
        stats['median'] = statistics.median(self.values())
        stats['mode'] = statistics.mode(self.values())
        stats['variance'] = statistics.variance(self.values())
        stats['stdev'] = statistics.stdev(self.values())
        return stats

    def serialize_to_json(self, filename):
        """
        Serialize the dictionary to JSON format and save it to a file.

        :param filename: The name of the file to save the JSON data to.
        """
        with open(filename, 'w') as f:
            json.dump(self, f)

    def serialize_to_csv(self, filename):
        """
        Serialize the dictionary to CSV format and save it to a file.

        :param filename: The name of the file to save the CSV data to.
        """
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.items())

    def deserialize_from_json(self, filename):
        """
        Deserialize the dictionary from JSON format.

        :param filename: The name of the file containing the JSON data.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            self.update(data)

    def deserialize_from_csv(self, filename):
        """
        Deserialize the dictionary from CSV format.

        :param filename: The name of the file containing the CSV data.
        """
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.update(dict(row))

    def update_with_condition(self, func):
        """
        Update dictionary values based on a condition.

        :param func: The updating function.
        """
        for k, v in self.items():
            self[k] = func(k, v)

    def search_and_replace(self, search_value, replace_value):
        """
        Search for specific values and replace them with another value.

        :param search_value: The value to search for.
        :param replace_value: The value to replace the searched value with.
        """
        for k, v in self.items():
            if v == search_value:
                self[k] = replace_value

    def key_validation(self, schema):
        """
        Validate keys against a given schema or pattern.

        :param schema: The schema or pattern to validate keys against.
        :return: A new dictionary containing only valid key-value pairs.
        """
        return Dict((k, v) for k, v in self.items() if schema(k))

    def group_by(self, key_func):
        """
        Group items in the dictionary by a specific key or criterion.

        :param key_func: The function to determine the grouping key.
        :return: A dictionary of grouped items.
        """
        grouped_dict = defaultdict(list)
        for k, v in self.items():
            grouped_dict[key_func(k, v)].append((k, v))
        return grouped_dict

    def delete(self, *keys):
        """
        Delete multiple keys and their corresponding values from the dictionary.

        :param keys: The keys to delete.
        """
        for key in keys:
            if key in self:
                del self[key]