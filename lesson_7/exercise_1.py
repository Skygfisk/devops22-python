import string

def do_nothing():
    pass
do_nothing()

def hello_world():
    print("hello world")

def is_same():
    print(1 == 1.0)

def revers_alphabet():
    print(string.ascii_uppercase[::-1])

def greeting(name):
    print(f'hello {name}')

def to_capital(word):
    print(word.upper())

def print_range(x):
    my_str = ""
    for n in range(1, x):
        my_str += str(n)
    print(my_str)