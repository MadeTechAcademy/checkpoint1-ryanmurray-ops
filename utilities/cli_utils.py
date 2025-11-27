from themes import Theme
from utilities.html_utils import save_duties_to_html

def get_prompt():
     return """
Welcome to apprentice themes!


Press (1) to list all the duties
Press (2) to generate an HTML file of duties
Press (3) to view duties by theme
Enter your choice:
"""

def print_available_themes(renderer):
    renderer.print("Available Themes:\n")
    for number,theme in Theme.all_themes.items():
        print(f"{number}. {theme.name}")

def generate_html(duties, output_file):
    # Generate a HTML file with the given duties
    save_duties_to_html(duties, output_file)
    return output_file

def generate_theme_file(theme_number):
    theme = Theme.all_themes[theme_number]
    output_file = f"{theme.name.lower().replace(' ', '_')}.html"
    generate_html(theme.duties, output_file)
    return output_file, theme.name 