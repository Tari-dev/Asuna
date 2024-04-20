# Asuna
A package with useful fucntions to help Hajime.

```shell
python -m pip install -U git+https://github.com/Hajime8673/Asuna
```

```py
from Asuna import Context

ctx = Context({'asuna': 10})
print(ctx.asuna)  # Output: 10
print(ctx.sakura)  # Output: None

ctx = Context({'asuna': 10}, default=0, miyuki=5)
print(ctx.asuna)  # Output: 10
print(ctx.sakura)  # Output: 0
print(ctx.miyuki)  # Output: 5
```

```py
from Asuna import Chunker

### chunk function example
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
result = Chunker.chunk(my_list, chunk_size)
print(result) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]


### multi_chunk function example
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
list3 = [9, 10, 11, 12]
result = Chunker.multi_chunk(list1, list2, list3, chunk_size=3, default_value=0)
print(result) # Output: [[1, 6, 9], [2, 7, 10], [3, 8, 11], [4, 0, 12], [5, 0, 0]]


### split function example
# Specify the number of sublists to split into
split_into = 4
# Split the list using the split function
result = Chunker.split(my_list, split_into)

# Display the result
print("Original List:", my_list)
print("Split into", split_into, "sublists:")
for i, sublist in enumerate(result):
    print(f"Sublist {i+1}: {sublist}")

## Output:
# Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Split into 4 sublists:
# Sublist 1: [1, 2, 3]
# Sublist 2: [4, 5, 6]
# Sublist 3: [7, 8]
# Sublist 4: [9, 10]
```

```py
from Asuna import RetryHandler

def test(a, b):
    return a + b

# Example for RetryHandler
if __name__ == "__main__":
    # RetryHandler will retry on error, when result type is not int or float and when result is 3
    retry_handler = RetryHandler(
        on_error=True, 
        on_type_unmatch=[int, float], 
        on_match=[3],
        retry_delay=3, 
        retries=2,
        delay_multiply=2)
    # retry_handler.retry decorator returns a function that takes the arguments of test function
    # The returned function will call test function and retry if necessary
    retry_function = retry_handler.retry(test)
    result = retry_function(1, 2)
    print(f"Result from RetryHandler: {result}")
```

```py
from Asuna import AsyncRetryHandler
import asyncio
# Example for AsyncRetryHandler

async def test(a, b):
    return a + b

def handler(result):
    """
    Example handler function that checks if result is equal to 3.
    """
    return result == 3

async def main():
    # AsyncRetryHandler will retry on error, when handler function returns True and when result is not 3
    retry_handler = AsyncRetryHandler(
        on_error=True,
        handler=handler,
        retry_delay=3,
        retries=3,
        delay_multiply=2)
    retry_function = retry_handler.retry(test)
    result = await retry_function(1, 2)
    print(f"Result from AsyncRetryHandler: {result}")

asyncio.run(main())
```

```py
from Asuna import List

# Create a List object
my_list = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Chunk the list into smaller sublists of size 3
chunked_list = my_list.chunk(3)
print("Chunked List (Chunk Size = 3):", chunked_list)

# Split the list into 4 smaller sublists
split_list = my_list.split(4)
print("Split List (Into 4 Sublists):", split_list)

# Shuffle the list
my_list.shuffle()
print("Shuffled List:", my_list)

# Get unique elements without preserving order
unique_list = my_list.unique()
print("Unique Elements (Order Not Preserved):", unique_list)

# Get unique elements preserving order
unique_list_preserve_order = my_list.unique(keep_order=True)
print("Unique Elements (Order Preserved):", unique_list_preserve_order)

# Flatten nested lists
nested_list = List([[1, 2], [3, 4, [5, 6]], 7, [8, [9, 10]]])
flattened_list = nested_list.flatten()
print("Flattened List:", flattened_list)

# Apply a function to each element
mapped_list = my_list.map(lambda x: x * 2)
print("Mapped List (Doubled):", mapped_list)

# Filter elements based on a condition
filtered_list = my_list.filter(lambda x: x % 2 == 0)
print("Filtered List (Even Numbers):", filtered_list)

# Reduce the list to a single value (sum)
sum_of_elements = my_list.reduce(lambda x, y: x + y)
print("Sum of Elements:", sum_of_elements)

# Search and replace elements
my_list.search_and_replace(5, 100)
print("List after Search and Replace (5 replaced with 100):", my_list)

# Merge multiple lists
list1 = List([1, 2, 3])
list2 = List([4, 5, 6])
merged_list = my_list.merge(list1, list2)
print("Merged List:", merged_list)

# Calculate basic statistics
stats = my_list.statistics()
print("Statistics:", stats)

# Serialize the list to JSON format
my_list.serialize_to_json("list_data.json")

# Deserialize the list from JSON format
deserialized_list = List()
deserialized_list.deserialize_from_json("list_data.json")
print("Deserialized List from JSON:", deserialized_list)

# Serialize the list to CSV format
my_list.serialize_to_csv("list_data.csv")

# Deserialize the list from CSV format
deserialized_list_csv = List()
deserialized_list_csv.deserialize_from_csv("list_data.csv")
print("Deserialized List from CSV:", deserialized_list_csv)
```

```py
from Asuna import Dict
# Create a Dict object
my_dict = Dict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

# Set default value for missing keys
my_dict.default_value(0)

# Merge dictionaries
merged_dict = my_dict.merge({'e': 5, 'f': 6}, {'g': 7, 'h': 8})
print("Merged Dictionary:", merged_dict)

# Filter keys and values based on a condition
filtered_dict = merged_dict.filter(lambda k, v: v % 2 == 0)
print("Filtered Dictionary:", filtered_dict)

# Apply a function to all values in the dictionary
mapped_dict = merged_dict.map_values(lambda v: v * 2)
print("Mapped Dictionary:", mapped_dict)

# Flatten nested dictionaries into a single-level dictionary
nested_dict = Dict({'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}})
flattened_dict = nested_dict.flatten()
print("Flattened Dictionary:", flattened_dict)

# Reverse the keys and values in the dictionary
reversed_dict = merged_dict.reverse()
print("Reversed Dictionary:", reversed_dict)

# Invert the dictionary, swapping keys and values
inverted_dict = merged_dict.invert()
print("Inverted Dictionary:", inverted_dict)

# Sort the dictionary based on keys
sorted_keys_dict = merged_dict.sort_keys()
print("Dictionary sorted by keys:", sorted_keys_dict)

# Sort the dictionary based on values
sorted_values_dict = merged_dict.sort_values()
print("Dictionary sorted by values:", sorted_values_dict)

# Calculate basic statistics for values in the dictionary
stats = merged_dict.statistics()
print("Statistics:", stats)

# Serialize the dictionary to JSON format
merged_dict.serialize_to_json("dict_data.json")

# Deserialize the dictionary from JSON format
deserialized_dict = Dict()
deserialized_dict.deserialize_from_json("dict_data.json")
print("Deserialized Dictionary from JSON:", deserialized_dict)

# Delete multiple keys and their corresponding values
deserialized_dict.delete_keys('e', 'f')
print("Dictionary after deleting keys 'e' and 'f':", deserialized_dict)

```

#### Note: Useful for development stage and may not be efficient for production environment.
