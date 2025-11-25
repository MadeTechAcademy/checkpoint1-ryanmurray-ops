from themes import list_duties

def get_prompt():
     return """
Welcome to apprentice themes!


Press (1) to list all the duties
Press (2) to generate an HTML file of duties
Enter your choice:
"""


def main(choice=None):
    if choice is None:
        choice = input(get_prompt())
    
    if str(choice) == '1':
        print(list_duties())

if __name__=="__main__":
    main()