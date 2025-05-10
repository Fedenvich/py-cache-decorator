from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args: Callable, **kwargs: Callable) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper
