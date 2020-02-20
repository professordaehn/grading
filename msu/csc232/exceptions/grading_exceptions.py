class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class CategoryError(Error):
    """Exception raised for errors with assignment category.

    Attributes:
        category -- category that raised this error
        message -- explanation of this error
    """

    def __init__(self, category, message):
        self.category = category
        self.message = message


class NumberError(Error):
    """Exception raised for errors with assignment category.

        Attributes:
            category -- category that raised this error
            message -- explanation of this error
        """

    def __init__(self, number, message):
        self.category = number
        self.message = message


class MethodError(Error):
    """Exception raised for errors with assignment category.

        Attributes:
            category -- category that raised this error
            message -- explanation of this error
        """

    def __init__(self, method, message):
        self.category = method
        self.message = message
