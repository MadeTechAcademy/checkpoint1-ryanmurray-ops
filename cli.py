from themes import list_duties, duties, themes
from utilities.cli_utils import generate_html, generate_theme_file, get_prompt, print_available_themes

def main(choice=None, theme_number=None):
    if choice is None:
        choice = input(get_prompt())
    
    if str(choice) == "1":
        print(list_duties())
    
    elif str(choice) == "2":
        output_file = "duties.html"
        generate_html(duties, output_file)
        print(f"Duties saved to {output_file}")
    
    elif str(choice) == "3":
        print_available_themes()

        if theme_number is None:
            theme_number = int(input("Enter theme number: "))

        output_file, theme_name = generate_theme_file(theme_number)
        print(f"Theme '{theme_name}' saved to {output_file}")

if __name__=="__main__":
    main()