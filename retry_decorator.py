"""Module to retry a function if an exception occurs"""
import time


class Retry(object):
    """
    Decorator for retrying function "tries" times if exception occurs
    """

    default_exceptions = Exception

    def __init__(self, tries, exceptions=None, delay=0):
        """
        Decorator for retrying function "tries" times if exception occurs

        tries - number of tries
        exceptions - exceptions to catch
        delay - wait between retries
        """
        self.tries = tries
        if exceptions is None:
            exceptions = Retry.default_exceptions
        self.exceptions = exceptions
        self.delay = delay

    def __call__(self, f):
        def fn_x(*args, **kwargs):
            exception = None
            for _ in range(self.tries):
                try:
                    return f(*args, **kwargs)
                except self.exceptions as def_exception:
                    time.sleep(self.delay)
                    exception = def_exception
            raise exception  # If no success raise an exception

        return fn_x  # true decorator
