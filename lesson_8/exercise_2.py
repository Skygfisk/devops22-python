def int_input(text):
    number = None
    while True:
        try:
            number = int(input(text))
            if (number%2 == 0):
                raise Exception('Even number is not allowed')
            break
        except ValueError:
            print("Sorry, not an int")
    return number


my_number = int_input("Enter a number: ")
print(f'result: {my_number}')