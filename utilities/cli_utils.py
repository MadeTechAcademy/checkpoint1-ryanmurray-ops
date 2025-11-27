from themes import Theme
from utilities.html_utils import save_duties_to_html
from rich_cli import RichRenderer
from rich.table import Table
from rich.console import Console
from rich.text import Text

def get_prompt(renderer=None):
     if isinstance(renderer, RichRenderer):
        table = Table(title="[bold magenta]Welcome to Apprentice Themes[/bold magenta]")
        table.add_column("Option", style="bold cyan", justify="center")
        table.add_column("Action", style="cyan")
        table.add_row("1", "List all the duties")
        table.add_row("2", "Generate an HTML file of duties")
        table.add_row("3", "View duties by theme")

        renderer.print(table)
        renderer.print(Text("Please choose an option: ", style="bold green"))
        return ""
     else:
        return (
            "Welcome to apprentice themes!\n\n"
            "Press (1) to list all the duties\n"
            "Press (2) to generate an HTML file of duties\n"
            "Press (3) to view duties by theme\n"
            "Enter your choice: "
        )

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

def render_specific_theme_duties(renderer, theme_number):
    theme = Theme.all_themes[theme_number]
    output_file, theme_name = generate_theme_file(theme_number)

    if isinstance(renderer, RichRenderer):
        console = Console()
        renderer.print(f"Theme '{theme_name}' saved to {output_file}, style=bold green")

        # Create a table with a title and lines between rows
        table = Table(title="Duties in '{theme_name}'", show_lines=True)
        table.add_column("Duty #", style="bold cyan", no_wrap=True)
        table.add_column("Description", style="cyan")

        for duty_number, duty_description in enumerate(theme.duties, start=1):
            table.add_row(f"{duty_number}", duty_description)

        console.print(table)
    else:
        renderer.print(f"Theme '{theme_name}' saved to {output_file}")
        renderer.print(f"Duties in '{theme_name}':")
        for duty_description in theme.duties:
            renderer.print(f"- {duty_description}")

