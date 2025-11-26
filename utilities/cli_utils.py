from themes import themes, duties
from utilities.html_utils import save_duties_to_html

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