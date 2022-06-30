import json


from light import settings


class Light:
    def __init__(self, routes):
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

light = Light(routes=settings.ROUTE_CONF)
