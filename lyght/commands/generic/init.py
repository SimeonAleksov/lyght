import click
import pyfiglet
from rich import print
from rich.prompt import Prompt, Confirm
from rich.tree import Tree


@click.command(name='init')
def init():
    tree = Tree("Generated project.")
    title = pyfiglet.figlet_format('Lyght', font='slant')
    print(f'[yellow]{title}[/yellow]')
    project_name = Prompt.ask("Enter your project name")
    author = Prompt.ask("Enter the project author")
    confirm = Confirm.ask("Do you want to generate Lyght project?")
    if confirm:
        pass

    tree.add(project_name).add('settings.py')
    tree.add('exec.py')
    tree.add('__init__.py')
    tree.add('README.md')
    print(tree)



if __name__ == '__main__':
    init()
