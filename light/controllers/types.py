import typing


from light.controllers.base import BaseController


BaseControllerType = typing.TypeVar("BaseControllerType", bound=BaseController)
