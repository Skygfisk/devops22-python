from statistics import median

name_1 = input("Please enter name for person 1: ").title()
age_1 = int(input("Please enter age for person 1: "))
size_1 = int(input("Please enter shoe size for person 1: "))

name_2 = input("Please enter name for person 2: ").title()
age_2 = int(input("Please enter age for person 2: "))
size_2 = int(input("Please enter shoe size for person 2: "))

name_3 = input("Please enter name for person 3: ").title()
age_3 = int(input("Please enter age for person 3: "))
size_3 = int(input("Please enter shoe size for person 3: "))

name = {"person_1" : name_1,
        "person_2" : name_2,
        "person_3" : name_3}
age = {"person_1" : age_1,
       "person_2" : age_2,
       "person_3" : age_3}
size = {"person_1" : size_1,
        "person_2" : size_2,
        "person_3" : size_3}
age_to_name = {age_1:name_1,
               age_2:name_2,
               age_3:name_3}
my_list = age_to_name.items()
my_list = list(my_list)
my_list.sort(reverse=True)
oldes_name = my_list[0]

age_to_size = {age_1:size_1,
               age_2:size_2,
               age_3:size_3}
my_list = age_to_size.items()
my_list = list(my_list)
my_list.sort(reverse=True)
oldest_size = my_list[0]

print(f'The oldest person is {oldes_name[1]} who has shoe size {oldest_size[1]}')

size_to_name = {size_1:name_1,
                size_2:name_2,
                size_3:name_3}
my_list = size_to_name.items()
my_list = list(my_list)
my_list.sort()
median_name = my_list[1]

size_to_age = {size_1:age_1,
               size_2:age_2,
               size_3:age_3}
my_list = size_to_age.items()
my_list = list(my_list)
my_list.sort()
median_age = my_list[1]
print(f'The person with median shoe size is {median_name[1]} who is {median_age[1]} years old')

