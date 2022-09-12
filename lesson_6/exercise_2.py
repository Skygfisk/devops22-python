import random
from operator import itemgetter

names = ["Adam", "Bertil", "Caesar", "David", "Erik",
         "Filip", "Gustav", "Helge", "Ivar", "Johan"]
hundred_names = random.choices(names, k=100)
print(len(hundred_names))
sorted_hundred_names = sorted(hundred_names)

count_names = {}
for vote in sorted_hundred_names:
    if vote in count_names:
        count_names[vote] += 1
    else:
        count_names[vote] = 1
print(count_names)

dict_items = count_names.items()
dict_items_sorted = sorted(dict_items, key=itemgetter(1), reverse=True)
print(f"Top 3 names: {dict_items_sorted[0:3]}")
print(f'Least popular name is: {dict_items_sorted[-1]}')

unique_names = list(set(hundred_names))
print(sorted(unique_names))
random.shuffle(unique_names)
print(unique_names)
print(sorted(unique_names, reverse=True))