def devision(x, y):
    if (type(y) == str):
        raise TypeError
    try:
        x/y
    except ZeroDivisionError:
        print("Division by zero is not alowed")
        return
    return x/y

print(devision(1, 1))