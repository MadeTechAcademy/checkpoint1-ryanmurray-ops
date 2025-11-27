from rich_cli import RichRenderer

def select_renderer(choice=None):
    if choice == "1":
        return RichRenderer()