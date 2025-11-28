from themes import Theme
from utilities.cli_utils import generate_html, generate_theme_file, get_prompt, print_available_themes, render_all_duties, render_duties_html, render_specific_theme_duties, get_theme_choice, get_main_choice
from standard_cli import StandardRenderer

def main(choice=None, theme_number=None, renderer=None):
    if renderer is None:
        renderer = StandardRenderer()

    if choice is None:
        get_prompt(renderer)
        choice = get_main_choice(renderer)
    
    if str(choice) == "1":
        render_all_duties(renderer)
    
    elif str(choice) == "2":
        render_duties_html(renderer)
    
    elif str(choice) == "3":
        print_available_themes(renderer)

        if theme_number is None:
            theme_number = get_theme_choice(renderer)
        render_specific_theme_duties(renderer, theme_number)

    else:
        renderer.print("Invalid choice, please select 1, 2 or 3")

if __name__=="__main__":
    main()