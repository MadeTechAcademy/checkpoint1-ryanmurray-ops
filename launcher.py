from rich_cli import RichRenderer
from cli import StandardRenderer, main

def select_renderer(choice=None):
    if choice == "1":
        return RichRenderer()
    else:
        return StandardRenderer()

def launch_selected_terminal(choice=None, renderer_choice=None):
    renderer = select_renderer(renderer_choice)
    main(choice=choice, renderer=renderer)