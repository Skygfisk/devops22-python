my_list = [x+1 for x in range(10)]
print(my_list)

y = lambda x: x+1
my_list = list(map(y, my_list))

print(my_list)
