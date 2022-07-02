import typing

import pydantic

from lyght.routes.route import Route


class Routes(
    typing.NamedTuple(
        'Routes',
        [
            ('routes', Route),
        ],
    )
):
    pass


__all__ = [
    "Route",
    "Routes",
]
