from themes import Theme
from utilities.html_utils import save_duties_to_html
from rich_cli import RichRenderer
from standard_cli import StandardRenderer
from rich.table import Table



# ----------------------------
# CLI Main Menu
# ----------------------------
# Display the main menu and prompt the user for a choice
def get_prompt(renderer=None):
     if isinstance(renderer, RichRenderer):
        table = Table(title="Welcome to Apprentice Themes",  title_style="bold magenta", border_style="bright_blue", show_lines=True)
        table.add_column("Option", style="bold cyan", justify="center")
        table.add_column("Action", style="cyan", justify="left")
        table.add_row("0", "List all the duties")
        table.add_row("1", "List all the duties")
        table.add_row("2", "Generate an HTML file of duties")
        table.add_row("3", "View duties by theme")
        table.add_row("4", "to Exit")

        renderer.print(table)
        return ""
     else:
        return (
            "Welcome to apprentice themes!\n\n"
            "Press (0) to list all the duties\n"
            "Press (1) to list all the duties\n"
            "Press (2) to generate an HTML file of duties\n"
            "Press (3) to view duties by theme\n"
            "Press (4) to Exit"
        )



# ----------------------------
# CLI Main Menu Helper: Get user choice
# ----------------------------
# Continuously prompt user until they enter a valid main menu option
# Works with any renderer, only prints error messages via renderer
def get_main_choice(renderer):
    while True:
        try:
            choice = int(input(("Please choose an option: ")))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                renderer.print("Invalid choice, please select 1, 2, 3 or 4", style="bold red")
        except ValueError:
            renderer.print("Please enter a valid number", style="bold red")



# ----------------------------
# CLI Main Menu Helper: Display menu and get choice
# ----------------------------
# Display the main menu using get_prompt() and return a valid main menu choice
# Uses get_prompt() and handles printing for StandardRenderer
def display_menu_and_get_choice(renderer=None):
    menu_text = get_prompt(renderer)
    if isinstance(renderer, StandardRenderer):
        print(menu_text)
    choice = get_main_choice(renderer)
    return choice

# ----------------------------
# CLI Option 0: Return to Launcher
# ----------------------------
# Display the main menu and prompt the user for a choice
def return_to_launcher():
    print("Returning to Launcher...")
    from launcher import launch_selected_terminal
    launch_selected_terminal()


# ----------------------------
# CLI Option 1: List All Duties
# ----------------------------
# Render all apprenticeship duties as a table or plain text
def render_all_duties(renderer):
    if isinstance(renderer, RichRenderer):
        table = Table(title="All Apprenticeship Duties", title_style="bold magenta", border_style="bright_blue", show_lines=True)
        table.add_column("Duty #", style="bold cyan", justify="center", no_wrap=True)
        table.add_column("Description", style="cyan", justify="left")
        for duty_number, duty_text in enumerate(Theme.all_duties, start=1):
            table.add_row(f"{duty_number}", duty_text)
        renderer.print(table)
    else:
        # Plain text for StandardRenderer
        renderer.print(Theme.list_duties())



# ----------------------------
# CLI Option 2: Generate HTML for All Duties
# ----------------------------
#Generate a HTML file containing all duties
def render_duties_html(renderer, output_file="duties.html"):
    generate_html(Theme.all_duties, output_file)
    renderer.print(f"Duties saved to {output_file}")        



# ----------------------------
# CLI Option 3a: List Available Themes
# ----------------------------
# Render a table of all available themes
def print_available_themes(renderer):
    if isinstance(renderer, RichRenderer):
        table = Table(title="Available Themes", title_style="bold magenta", border_style="bright_blue", show_lines=True,)
        table.add_column("Number", style="bold cyan", justify="center")
        table.add_column("Theme Name", style="cyan", justify="left")
        for number,theme in Theme.all_themes.items():
            table.add_row(f"{number}", theme.name)
        renderer.print(table)
    else:
        renderer.print("Available Themes:\n")
        for number, theme in Theme.all_themes.items():
            renderer.print(f"{number}. {theme.name}")



# ----------------------------
# CLI Option 3a Helper: Prompt user for Theme Selection
# ----------------------------
# Continuously prompt the user until a valid theme number is entered
def get_theme_choice(renderer):
    while True:
        try:
            choice = int(input("Please choose an option: "))
            if choice in Theme.all_themes:
                return choice
            else:
                renderer.print("Invalid theme number, please try again", style="bold red")
        except ValueError:
            renderer.print("Please enter a valid number", style="bold red")



# ----------------------------
# CLI Option 3b: Render Duties for a Specific Theme
# ----------------------------
# Render duties for a specific theme and generate HTML file
def render_specific_theme_duties(renderer, theme_number):
    theme = Theme.all_themes[theme_number]
    output_file, theme_name = generate_theme_file(theme_number)

    if isinstance(renderer, RichRenderer):
        renderer.print(f"Theme '{theme_name}' saved to {output_file}", style="bold green")

        # Create a table with a title and lines between rows
        table = Table(title=f"Duties in '{theme_name}'", title_style="bold magenta", border_style="bright_blue", show_lines=True)
        table.add_column("Duty #", style="bold cyan", justify="center", no_wrap=True)
        table.add_column("Description", style="cyan", justify="left")
        for duty_number, duty_description in enumerate(theme.duties, start=1):
            table.add_row(f"{duty_number}", duty_description)
        renderer.print(table)
    else:
        renderer.print(f"Theme '{theme_name}' saved to {output_file}")
        renderer.print(f"Duties in '{theme_name}':")
        for duty_description in theme.duties:
            renderer.print(f"- {duty_description}")



# ----------------------------
# Utilities: HTML Generation (used by Options 2 and 3)
# ----------------------------
# Save a list of duties to a HTML file
def generate_html(duties, output_file):
    save_duties_to_html(duties, output_file)
    return output_file



# Generate a HTMl file for a specific theme and return its file name
def generate_theme_file(theme_number):
    theme = Theme.all_themes[theme_number]
    output_file = f"{theme.name.lower().replace(' ', '_')}.html"
    generate_html(theme.duties, output_file)
    return output_file, theme.name 





