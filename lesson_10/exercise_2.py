class Dog:
    def __init__(self, name) -> None:
        self.name = name

MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'

1: 'Create'
2: 'Print'
3: 'Delete'
"""
my_dog = False
while True:
    print(MAIN_MENU_TEXT)
    choice = int(input("Enter your choice [1-3]: "))
    if choice == 1:
        my_dog = Dog("Justus")
        print("New object created")
    elif choice == 2:
        if my_dog == False:
            print("No object available to print")
        else:
            print(my_dog.name)
    elif choice == 3:
        if my_dog == False:
            print("No object to delete")
        else:
            my_dog = False
            print("Object deleted")
