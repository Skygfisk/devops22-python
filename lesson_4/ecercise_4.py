from re import S


str = input("Typ a star and stop number: ").split()
n1 = int(str[0])
n2 = int(str[1])
my_sum = 0

while n1 <= n2:
    print(n1)
    my_sum += n1
    n1 += 1

print(f'sum: {my_sum}')