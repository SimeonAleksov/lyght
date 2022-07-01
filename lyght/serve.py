import asyncio

import click

from lyght.http import server


@click.command()
@click.option('--host', '-h', default='127.0.0.1', help='Host to run the web server.')
@click.option('--port', '-p', default=5000, help='Port to run the web server.')
@click.option('--log_level', default='info', help='Log level.')
def main(host: str, port:int , log_level: str):
    _server = server.Server(host=host, port=port, log_level=log_level)
    asyncio.run(_server.serve())

if __name__ == "__main__":
    main()  # pragma: no cover
