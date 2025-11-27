from themes import Theme
from utilities.html_utils import save_duties_to_html
from rich_cli import RichRenderer
from rich.table import Table
from rich.console import Console

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

def render_all_duties(renderer):
    # Display all apprenticeship duties using the given renderer.
    # RichRenderer: styled output
    # StandardRenderer: plain text
    if isinstance(renderer, RichRenderer):

        console = Console()

        # Create a table with a title and lines between rows
        table = Table(title="All Apprenticeship Duties", show_lines=True)
        table.add_column("Duty #", style="bold cyan", no_wrap=True)
        table.add_column("Description", style="cyan")

        for duty_number, duty_text in enumerate(Theme.all_duties, start=1):
            table.add_row(f"{duty_number}", duty_text)

        console.print(table)

    else:
        # Plain text for StandardRenderer
        renderer.print(Theme.list_duties())

def render_duties_html(renderer, output_file="duties.html"):
    generate_html(Theme.all_duties, output_file)
    renderer.print(f"Duties saved to {output_file}")