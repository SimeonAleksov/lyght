import click
import pyfiglet
from rich import print


@click.command(name='init')
def init():
    title = pyfiglet.figlet_format('Lyght', font='slant')
    print(f'[yellow]{title}[/yellow]')


if __name__ == '__main__':
    init()
