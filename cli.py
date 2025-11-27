from themes import Theme
from utilities.cli_utils import generate_html, generate_theme_file, get_prompt, print_available_themes
from standard_cli import StandardRenderer

def main(choice=None, theme_number=None, renderer=None):
    if renderer is None:
        renderer = StandardRenderer()

    if choice is None:
        choice = input(get_prompt())
    
    if str(choice) == "1":
        renderer.print(Theme.list_duties())
    
    elif str(choice) == "2":
        output_file = "duties.html"
        generate_html(Theme.all_duties, output_file)
        renderer.print(f"Duties saved to {output_file}")
    
    elif str(choice) == "3":
        print_available_themes(renderer)

        if theme_number is None:
            theme_number = int(input("Enter theme number: "))

        output_file, theme_name = generate_theme_file(theme_number)

        renderer.print(f"Theme '{theme_name}' saved to {output_file}")
        renderer.print(f"Duties in '{theme_name}':")
        for duty in Theme.all_themes[theme_number].duties:
            renderer.print(f"- {duty}")
    
    else:
        renderer.print("Invalid choice, please select 1, 2 or 3")

if __name__=="__main__":
    main()