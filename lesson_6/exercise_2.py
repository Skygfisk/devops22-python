import random
from collections import Counter
from operator import itemgetter

names = ["Adam", "Bertil", "Caesar", "David", "Erik",
         "Filip", "Gustav", "Helge", "Ivar", "Johan"]
hundred_names = random.choices(names, k=100)
print(len(hundred_names))
sorted_hundred_names = sorted(hundred_names)

count_names = Counter(sorted_hundred_names)
print(count_names)

print(f'Top 3 names: {count_names.most_common(3)}')
print(f'Least popular name is: {count_names.most_common()[-1]}')

unique_names = list(set(hundred_names))
print(sorted(unique_names))
random.shuffle(unique_names)
print(unique_names)
print(sorted(unique_names, reverse=True))