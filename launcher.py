from rich_cli import RichRenderer
from cli import StandardRenderer, main

def select_renderer(choice=None):
    if choice == "1":
        return RichRenderer()
    elif choice == "2":
        return StandardRenderer()
    else:
        return StandardRenderer()
   

def launch_selected_terminal(choice=None, renderer_choice=None):
    renderer = select_renderer(renderer_choice)
    if choice not in ["1", "2"]:
        renderer.print("Invalid choice, please select 1 or 2")
        return

    main(choice=choice, renderer=renderer)