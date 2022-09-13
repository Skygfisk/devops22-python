def get_int(x):
    return int(x)

def get_tuple(x, y):
    return (x, y)

def is_true(x):
    return bool(x)

def get_float(x):
    return float(x)

def full_name(firstname, lastname):
    return str(firstname) + " " + str(lastname)

def square_area(x):
    return float(x)**2

def sum_of_list(x):
    return sum(x)

def repeat_word(word, repeat):
    for x in range(repeat):
        print(word)