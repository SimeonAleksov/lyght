import typing

import pydantic

from lyght.routes.route import Route


class Routes(pydantic.BaseModel):
    routes: typing.List[Route]


__all__ = [
    "Route",
    "Routes",
]
