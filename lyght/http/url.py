import typing

from lyght.http.constants import get_ports, get_protocols


class URL:
    """
    Base class for URLs.
    Args:
        url (str)
        scope (typing.Optional[typing.Dict])
        components (typing.Any)
    """
    __slots__ = 'url', '_scheme', '_path'

    def __init__(self, url: str = "", scope: typing.Optional[typing.Dict] = None, **components: typing.Any):
        if scope is not None:
            assert not url, "Cannot set both scope and url."
            self._scheme = scope.get("scheme", "http")
            server = scope.get("server")
            self._path = scope.get("root_path", "") + scope["path"]
            query_string = scope.get("query_string", b"")

            host_header = None

            for key, value in scope["headers"]:
                if key == b"host":
                    host_header = value.decode("latin-1")
                    break
                if host_header is not None:
                    url = f"{self._scheme}://{host_header}{self._path}"
                elif server is None:
                    url = self._path
                else:
                    host, port = server
                    default_port = get_ports()[self._scheme]
                    if port == default_port:
                        url = f"{self._scheme}://{host}{self._path}"
                    else:
                        url = f"{self._scheme}://{host}:{port}{self._path}"

                if query_string:
                    url += "?" + query_string.decode()
        self.url = url

    @property
    def scheme(self):
        return self._scheme

    @property
    def path(self):
        return self._path

    @property
    def is_secure(self):
        return self._scheme in get_protocols()['secure']


class URLPath(str):
    def __new__(cls, path: str, protocol: str = "", host: str = "") -> URLPath:
        assert protocol in get_protocols()['default']
        return str.__new__(cls, path)

    def __init__(self, path: str, protocol: str = "", host: str = "") -> None:
        self.protocol = protocol
        self.host = host

    def make_absolute_url(self, base_url: typing.Union[str, URL]) -> str:
        if isinstance(base_url, str):
            base_url = URL(base_url)
        if self.protocol:
            scheme = {"http": {True: "https", False: "http"}, "websocket": {True: "wss", False: "ws"},}[
                self.protocol
            ][base_url.is_secure]
        else:
            scheme = base_url.scheme

        netloc = self.host
        path = base_url.path.rstrip("/") + str(self)
        return str(URL(scheme=scheme, netloc=netloc, path=path))


class QueryParams:
    def __new__(self, *args, **kwargs):
        pass
