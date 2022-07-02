import re
import typing
import inspect


def get_default_route_name(controller: typing.Callable):
    if inspect.isroutine(controller) or inspect.isclass(controller):
        return controller.__name__
    return controller.__class__.__name__
