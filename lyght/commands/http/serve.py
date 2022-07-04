import asyncio

import click

from lyght.http.server import Server


@click.command()
@click.option("--hostname", "-h", default="localhost", help="Host to serve your app at.")
@click.option("--port", "-p", default=5000, help="Port to serve your app at.")
@click.option("--log_level", "-L", default="info", help="Log level.")
def serve(hostname, port, log_level):
    _server = Server(host=hostname, port=port, log_level=log_level)
    asyncio.run(_server.serve())



if __name__ == "__main__":
    serve()
