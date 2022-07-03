import typing

from lyght.http.status import HTTPStatus


class BaseResponse:
    content_type = None
    _charset = "utf-8"

    def __init__(
        self,
        data: typing.Any = None,
        status_code: typing.Optional[HTTPStatus] = None,
        headers: typing.Any = None,
    ):
        self.data = data
        self.status_code = status_code
        self.body = self.render_data()

    def render_data(self):
        if self.data is None:
            return b""
        if isinstance(self.data, bytes):
            return self.data

        return self.data.encode(self._charset)
