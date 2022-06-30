import asyncio

import click

from light.http import server


@click.command()
def main():
    _server = server.Server(port=5000, log_level='debug')
    asyncio.run(_server.serve())

if __name__ == "__main__":
    main()  # pragma: no cover
