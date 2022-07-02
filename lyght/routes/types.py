import typing
import uuid
from functools import lru_cache


T = typing.TypeVar("T")


class Converter:
    regex: typing.ClassVar[str] = ""

    def to_python(self, value: str) -> T:
        raise NotImplementedError()

    def to_route(self, value: T) -> str:
        raise NotImplementedError()



class IntConverter(Converter):
    regex = "[0-9]+"

    def to_python(self, value):
        return int(value)

    def to_route(self, value):
        return str(value)


class StringConverter(Converter):
    regex = "[^/]+"

    def to_python(self, value):
        return value

    def to_route(self, value):
        return value


class UUIDConverter(Converter):
    regex = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

    def to_python(self, value):
        return uuid.UUID(value)

    def to_route(self, value):
        return str(value)


class SlugConverter(StringConverter):
    regex = "[-a-zA-Z0-9_]+"


class PathConverter(StringConverter):
    regex = ".+"


DEFAULT_CONVERTERS = {
    "int": IntConverter(),
    "path": PathConverter(),
    "slug": SlugConverter(),
    "str": StringConverter(),
    "uuid": UUIDConverter(),
}


REGISTERED_CONVERTERS = {}


def register_converter(converter, type_name):
    REGISTERED_CONVERTERS[type_name] = converter()
    get_converters.cache_clear()


@lru_cache(maxsize=None)
def get_converters():
    return {**DEFAULT_CONVERTERS, **REGISTERED_CONVERTERS}


def get_converter(raw_converter):
    return get_converters()[raw_converter]
