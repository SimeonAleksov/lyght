class BaseHTTPException(Exception):
    """
    Base exception class used for all http errors.
    """


class InvalidHTTPConnectionError(BaseHTTPException):
    pass
