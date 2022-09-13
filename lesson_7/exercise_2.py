def print_range(x=1, y=11):
    my_str = ""
    for n in range(x, y):
        my_str += str(n)
    print(my_str)

def print_string(word, reverse=False):
    if reverse == True:
        print(word[::-1])
    else:
        print(word)
print_string("QWERTY")
print_string("QWERTY", reverse=True)