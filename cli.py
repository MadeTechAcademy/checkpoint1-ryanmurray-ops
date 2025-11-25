from themes import list_duties, duties
from utilities.cli_utils import generate_html

def get_prompt():
     return """
Welcome to apprentice themes!


Press (1) to list all the duties
Press (2) to generate an HTML file of duties
Press (3) to view duties by theme
Enter your choice:
"""


def main(choice=None):
    if choice is None:
        choice = input(get_prompt())
    
    if str(choice) == "1":
        print(list_duties())
    
    elif str(choice) == "2":
        output_file = "duties.html"
        generate_html(duties, output_file)
        print(f"Duties saved to {output_file}")
    
    elif str(choice) == "3":
        themes = ["Bootcamp", "Automate!", "Houston, Prepare to Launch", "Going Deeper", "Assemble", "Call Security"]
        print("\n".join(themes))

if __name__=="__main__":
    main()