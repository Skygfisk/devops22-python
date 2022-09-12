import random

one_to_hundred = [x for x in range(1, 101)]
print(one_to_hundred)

even = one_to_hundred[1:61:2]
print(even)

odd = one_to_hundred[0:77:2]
print(odd)

one_to_three_hundred_unique = [x for x in range(1, 301, 3)]
print(one_to_three_hundred_unique)
print(len(one_to_three_hundred_unique))

one_to_three_hundred = [x for x in range(1, 301)]
one_to_three_hundred_random = random.sample(one_to_three_hundred, k=100)
print(one_to_three_hundred_random)
print(len(one_to_three_hundred_random))

no_red = ["Yellow", "Blue", "Green", "Black", "White"]
red = ["Red"]
red.extend(random.sample(no_red, k=2))
print(red)
fifty_color = random.choices(red, k=50)
print(fifty_color)
print(f'The list red contain {len(red)} element and the unique colors {set(red)}')
print(f'The list no_red contain {len(no_red)} element and the unique colors {set(no_red)}')
print(f'The list fifty_color contain {len(fifty_color)} element and the unique colors {set(fifty_color)}')