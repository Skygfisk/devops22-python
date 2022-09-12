list_1 = ["Adam", "Bertil", "Caesar", "David"]
list_2 = list_1
list_3 = list_1.copy()

list_1.pop()
list_1.append("Zek")

print(list_1)
print(list_2)
print(list_3)