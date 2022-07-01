import json

from lyght.config import settings
from lyght.routes import Routes



class Lyght:
    def __init__(self, routes: Routes):
        self.routes = routes

    async def __call__(self, scope, receive, send):
        assert scope['type'] == 'http'

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'application/json'],
            ],
        })

        await send({
            'type': 'http.response.body',
            'body': json.dumps({"message": f"Hello from {scope['path']}!"}).encode('utf-8'),
        })


lyght = Lyght(routes=settings.ROUTE_CONF)
