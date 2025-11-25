from themes import list_duties, duties, themes
from utilities.cli_utils import generate_html

def get_prompt():
     return """
Welcome to apprentice themes!


Press (1) to list all the duties
Press (2) to generate an HTML file of duties
Press (3) to view duties by theme
Enter your choice:
"""


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
        if theme_number is None:
            print("Available Themes:\n")
            for number, (theme_name, duty_numbers) in themes.items():
                print(f"{number}. {theme_name}")

        else:
            theme_name, duty_numbers = themes[theme_number]
            theme_duties = [duties[i - 1] for i in duty_numbers]

            output_file = f"{theme_name.lower().replace(' ', '_')}.html"
            generate_html(theme_duties, output_file)

            print(f"Theme '{theme_name}' saved to {output_file}")
        # themes = ["Bootcamp", "Automate!", "Houston, Prepare to Launch", "Going Deeper", "Assemble", "Call Security"]
        # print("\n".join(themes))

if __name__=="__main__":
    main()