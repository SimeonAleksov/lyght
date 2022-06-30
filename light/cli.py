"""Console script for light."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("light")
    click.echo("=" * len("light"))
    click.echo("Lighting fast python web framework.")


if __name__ == "__main__":
    main()  # pragma: no cover
