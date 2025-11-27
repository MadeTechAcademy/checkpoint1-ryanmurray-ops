from rich_cli import RichRenderer
from cli import StandardRenderer, main

def select_renderer(choice=None):
    if choice == "1":
        return RichRenderer()
    else:
        return StandardRenderer()
   

def launch_selected_terminal(choice=None, renderer_choice=None):
    # Welcome Message
    print("=" * 50)
    print("WELCOME TO APPRENTICE THEMES TERMINAL".center(50))
    print("=" * 50 + "\n")

    # Prompt for renderer
    if renderer_choice is None:
        print("Choose output mode:")
        print("1) Rich Mode (colorful, enhanced output)")
        print("2) Standard Mode (plain terminal output)")
        renderer_choice = input("Please Enter your preferred terminal (1 or 2): ")

    renderer = select_renderer(renderer_choice)

    if renderer_choice not in ["1", "2"]:
        renderer.print("Invalid choice, please select 1 or 2")
        return

    main(choice=choice, renderer=renderer)

if __name__ == "__main__":
    launch_selected_terminal()