from themes import list_duties

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