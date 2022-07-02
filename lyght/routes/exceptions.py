class BaseRouteException(Exception):
    """
    Base exception used for route exceptions.
    """
    pass


class InvalidRouteNameError(BaseRouteException):
    pass


class InvalidControllerInstance(BaseRouteException):
    pass


class DuplicatePathParamError(BaseRouteException):
    pass
