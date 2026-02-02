import time
import functools
from selenium.common.exceptions import (StaleElementReferenceException,ElementClickInterceptedException,
    TimeoutException,NoSuchElementException)


DEFAULT_EXCEPTIONS = (StaleElementReferenceException,ElementClickInterceptedException,
    TimeoutException,NoSuchElementException)

def retry(retries=2,delay=1,exceptions=DEFAULT_EXCEPTIONS,raise_last_exception=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, retries + 2):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exception = exc
                    if attempt > retries:
                        break
                    time.sleep(delay)

            if raise_last_exception and last_exception:
                raise last_exception

            return None

        return wrapper

    return decorator