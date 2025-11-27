from rich_cli import RichRenderer
from cli import StandardRenderer

def select_renderer(choice=None):
    if choice == "1":
        return RichRenderer()
    else:
        return StandardRenderer()