the_list = ("Adam", "Bertil", "Cesar", "David", "Erik")
x = input("Type your name: ").title()

if (x in the_list):
    print(f'Welcome {x}, you are on the list')
else:
    print("Sorry, you are not on the list")
