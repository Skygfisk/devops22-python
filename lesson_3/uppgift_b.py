from statistics import median

name_1 = input("Please enter name for person 1: ")
age_1 = input("Please enter age for person 1: ")
size_1 = input("Please enter shoe size for person 1: ")

name_2 = input("Please enter name for person 2: ")
age_2 = input("Please enter age for person 2: ")
size_2 = input("Please enter shoe size for person 2: ")

name_3 = input("Please enter name for person 3: ")
age_3 = input("Please enter age for person 3: ")
size_3 = input("Please enter shoe size for person 3: ")

name = {"person_1" : name_1,
        "person_2" : name_2,
        "person_3" : name_3}
age = {"person_1" : age_1,
       "person_2" : age_2,
       "person_3" : age_3}
size = {"person_1" : size_1,
        "person_2" : size_2,
        "person_3" : size_3}
oldest = max(age, key = lambda k: age[k])
print(f'The oldest person is {name[oldest].title()} who has shoe size {size[oldest]}')

med_size = median(size.values())
rev_size = {v: k for k, v in size.items()}
med_size_key = rev_size.get(med_size)
print(f'The person with median shoe size is {name[med_size_key]} who is {age[med_size_key]} years old')

str = input("Please enter search value, name, age or size followed by value: ")
x = str.split()