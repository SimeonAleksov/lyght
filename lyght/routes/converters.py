import datetime
import typing
import uuid
from functools import lru_cache


T = typing.TypeVar("T")


class Converter:
    regex: typing.ClassVar[str] = ""

    def to_python(self, value: str) -> T:
        raise NotImplementedError()

    def to_route(self, value: T) -> T:
        raise NotImplementedError()



class IntConverter:
    regex = "[0-9]+"

    def to_python(self, value):
        return int(value)

    def to_route(self, value):
        return str(value)


class StringConverter:
    regex = "[^/]+"

    def to_python(self, value):
        return value

    def to_route(self, value):
        return value


class UUIDConverter:
    regex = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

    def to_python(self, value):
        return uuid.UUID(value)

    def to_route(self, value):
        return str(value)


class SlugConverter(StringConverter):
    regex = "[-a-zA-Z0-9_]+"


class PathConverter(StringConverter):
    regex = ".+"


class DateTimeConverter(Converter):
    regex = "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(.[0-9]+)?"

    def to_python(self, value: str) -> datetime.datetime:
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")

    def to_route(self, value: datetime.datetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%S")


DEFAULT_CONVERTERS = {
    "int": IntConverter(),
    "path": PathConverter(),
    "slug": SlugConverter(),
    "str": StringConverter(),
    "uuid": UUIDConverter(),
    "datetime": DateTimeConverter(),
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
