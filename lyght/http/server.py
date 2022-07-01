import uvicorn

from lyght.config import settings


class Server:
    def __init__(self, host: str, port: int, log_level: str) -> None:
        config = uvicorn.Config(
            app=settings.ASGI_APPLICATION,
            host=host,
            port=port,
            log_level=log_level,
            reload=settings.DEBUG,
            use_colors=settings.DEBUG,
        )
        self._server = uvicorn.Server(config)

    async def serve(self):
        await self._server.serve()
