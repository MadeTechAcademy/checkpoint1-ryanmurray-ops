from themes import list_duties

def get_prompt():
     return """
Welcome to apprentice themes!


Press (1) to list all the duties
Press (2) to generate an HTML file of duties
Enter your choice:
"""


def main():
    x = input("""
    Welcome to apprentice themes!\n

    Press (1) to list all the duties\n
    Enter your choice:
    """)
    
    if x == '1':
        print(list_duties())

if __name__=="__main__":
    main()