import typing

from lyght.http.exceptions import InvalidHTTPConnectionError
from lyght.http.url import URL


class HTTPConnection:
    """
    Base class for incoming connections.
    Args:
        scope: Request scope
    Raises:
        lyght.http.exceptions.InvalidHTTPConnectionError
    """

    __eq__ = object.__eq__
    __hash__ = object.__hash__

    def __init__(self, scope) -> None:
        self._validate_scope(scope=scope)
        self.scope = scope

    @classmethod
    def _validate_scope(cls, scope):
        if scope['type'] not in []:
            raise InvalidHTTPConnectionError(f"Received invalid HTTP connection - {scope['type']}.")

    def __getitem__(self, key: str) -> typing.Any:
        return self.scope[key]

    def __iter__(self) -> int:
        return iter(self.scope)

    def __len__(self) -> int:
        return len(self.scope)

    @property
    def app(self):
        return self.scope['app']

    @property
    def url(self) -> URL:
        if not hasattr(self, "_url"):
            self._url = URL(scope=self.scope)
        return self._url

    @property
    def base_url(self) -> URL:
        if not hasattr(self, "_base_url"):
            base_url_scope = dict(self.scope)
            base_url_scope.update(
                {
                    "path": "/",
                    "query_string": b"",
                    "root_path": base_url_scope.get(
                        "app_root_path",
                        base_url_scope.get("root_path", ""),
                    ),
                }
            )
            self._base_url = URL(scope=base_url_scope)
        return self._base_url
