import json
import typing

from lyght.http.exceptions import InvalidHTTPConnectionError, ClientDisconnectedError
from lyght.http.types import Scope, Receive, Send, Http
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

    def __init__(self, scope: Scope) -> None:
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

    @property
    def query_params(self):
        self._query_params = self.scope["query_string"]
        return self._query_params

    @property
    def path_params(self):
        return self.scope.get("path_params")


class Request(HTTPConnection):
    __slots__ = ["method", "receive",]

    def __init__(self, scope: Scope, receive: Receive, send: Send) -> None:
        super().__init__(scope)
        self._validate_scope(scope=scope)
        self._receive = receive
        self._send = send
        self.method = self.scope["method"]
        self.receive = self.scope["receive"]

    async def stream(self) -> typing.AsyncGenerator[bytes, None]:
        if hasattr(self, "_body"):
            yield self._body
            yield b""
            return

        if self._stream_consumed:
            raise RuntimeError("Stream consumed")

        self._stream_consumed = True
        while True:
            message = await self._receive()
            if message["type"] == Http.REQUEST.value:
                body = message.get("body", b"")
                if body:
                    yield body
                if not message.get("more_body", False):
                    break
            elif message["type"] == Http.DISCONNECT.value:
                self._is_disconnected = True
                raise ClientDisconnectedError()
        yield b""

    async def body(self) -> bytes:
        if not hasattr(self, "_body"):
            chunks: "typing.List[bytes]" = []
            async for chunk in self.stream():
                chunks.append(chunk)
            self._body = b"".join(chunks)
        return self._body

    async def json(self) -> typing.Any:
        if not hasattr(self, "_json"):
            body = await self.body()
            self._json = json.loads(body)
        return self._json
