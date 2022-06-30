import uvicorn

from light import utils

settings = utils.import_settings()


class Server:
    def __init__(self, port: int, log_level: str) -> None:
        config = uvicorn.Config(
            app=settings.ASGI_APPLICATION,
            port=port,
            log_level=log_level,
            reload=settings.DEBUG,
        )
        self._server = uvicorn.Server(config)

    async def serve(self):
        await self._server.serve()
