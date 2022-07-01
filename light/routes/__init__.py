import typing

import pydantic

from light.routes import exceptions as routes_exceptions
from light.controllers import BaseController


class Route(pydantic.BaseModel):
    path: str
    name: str
    controller: typing.Type[BaseController]

    @pydantic.validator('path')
    def path_must_start_with_slash(cls, v):
        if not v.startswith('/'):
            raise routes_exceptions.InvalidRouteNameError(f'Route(path={v}) name must start with a slash(/).')
        return v


class Routes(pydantic.BaseModel):
    routes: typing.List[Route]
