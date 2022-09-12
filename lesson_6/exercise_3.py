from audioop import reverse
import string

abc = list(string.ascii_lowercase)
stack = []
str = ""

for x in abc:
    stack.append(x)

print(stack)

for x in range(len(stack)):
    str += stack[-1]
    stack.pop()

print(stack)
print(str)
