import typing
import re

from lyght.routes import exceptions as routes_exceptions
from lyght.routes.utils import get_default_route_name

from lyght.routes.constants import ROUTE_PARAM_REGEX
from lyght.routes.converters import get_converter


class Route:
    """
    Base class for lyght routing.
    Args:
        path (str): Route path, e.g. /user/profile.
        controller (typing.Callable): Controller that handles what happens to that route.
        name (str) Name for easier reverse searching for this route.
    Raises:
        lyght.routes.exceptions.DuplicatePathParamEror
    """

    def __init__(
        self,
        path: str,
        controller: typing.Callable,
        name: typing.Optional[str],
    ) -> None:
        self._path_must_start_with_slash(path)
        self.path = path
        self.controller = controller
        self.name = name or get_default_route_name(controller=controller)

        self.path_regex, self.path_format, self.path_converter = self._compile_route_path()

    def match(self):
        pass

    def _compile_route_path(self):
        is_host = not self.path.startswith("/")

        path_regex = "^"
        path_format = ""
        duplicated_params = set()

        idx = 0
        param_converters = {}
        for match in ROUTE_PARAM_REGEX.finditer(self.path):
            param_name, converter_type = match.groups("str")
            converter_type = converter_type.lstrip(":")
            converter = get_converter(converter_type)

            path_regex += re.escape(self.path[idx : match.start()])
            path_regex += f"(?P<{param_name}>{converter.regex})"

            path_format += self.path[idx : match.start()]
            path_format += "{%s}" % param_name

            if param_name in param_converters:
                duplicated_params.add(param_name)

            param_converters[param_name] = converter

            idx = match.end()

        if duplicated_params:
            names = ", ".join(sorted(duplicated_params))
            ending = "s" if len(duplicated_params) > 1 else ""
            raise routes_exceptions.DuplicatePathParamError(
                f"Duplicated paramater name{ending} {names} at path {self.path}"
            )

        if is_host:
            hostname = self.path[idx:].split(":")[0]
            path_regex += re.escape(hostname) + "$"
        else:
            path_regex += re.escape(self.path[idx:]) + "$"

        path_format += self.path[idx:]

        return re.compile(path_regex), path_format, param_converters

    @classmethod
    def _path_must_start_with_slash(cls, path):
        if not path.startswith('/'):
            raise routes_exceptions.InvalidRouteNameError(f'Route(path={path}) name must start with a slash(/).')
