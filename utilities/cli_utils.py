from themes import themes, duties
from utilities.html_utils import save_duties_to_html

def get_prompt():
     return """
Welcome to apprentice themes!


Press (1) to list all the duties
Press (2) to generate an HTML file of duties
Press (3) to view duties by theme
Enter your choice:
"""

def generate_html(duties, output_file):
    # Generate a HTML file with the given duties
    save_duties_to_html(duties, output_file)
    return output_file

def generate_theme_file(theme_number):
    theme_info = themes[theme_number]
    theme_name = theme_info[0]
    duty_numbers = theme_info[1]
    theme_duties = [duties[i - 1] for i in duty_numbers]
    output_file = f"{theme_name.lower().replace(' ', '_')}.html"
    generate_html(theme_duties, output_file)
    return output_file, theme_name 