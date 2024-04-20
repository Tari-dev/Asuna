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

#### Note: Useful for development stage and may not be efficient for production environment.
