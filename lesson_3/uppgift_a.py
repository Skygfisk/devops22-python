X = 1
Y = 4

addresses = {"Bella": "Klockgatan 1",
          "Cornelia": "Vikingagatan 3",
              "Adam": "Ormvägen 5",}

cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

# 5.1 
my_list = sorted(addresses.items()) # vi gör om 'addreses' till en lista av tuplar som är sorterad alfabetisk
my_entry = my_list[-1] # vi tar sista tubeln i listan
print(f'{my_entry[1]}') # vi printar andra värdet i tupeln som är addressen

# 5.2
my_dict = {v: k for k, v in addresses.items()} # vi bytter plats på key och values
my_dict = sorted(my_dict.items()) # vi gör om 'my_dict' till en lista av tuplar som är sorterad alfabetisk
my_addres = my_dict[0] # vi tar första tubeln i listan
print(f'{my_addres[1]}') # vi printar andra värdet i tupeln som är namnet

cars_2 = cars
cars.append("Saab")

# 10.1
cars_3 = cars.copy() # vi skapar en kopia av 'cars'
# 10.2
cars.extend(cars_3) # vi förlänger 'cars' med inehålet i 'cars_3'
cars.sort(reverse=True) # vi sorterar 'cars' i ovmändbokstavsordning
# 10.3
unique_cars = list(dict.fromkeys(cars)) # vi konverterar 'cars' till ett dict, efter som dict inte kan ha dubletter så försviner dom, sen converterar vi tillbaka till en list

numbers3 = numbers1.symmetric_difference(numbers2)
print(f'{numbers3}')
# 1. 'X' och 'Y' har datatypen int
# 2. 'addresses' har datatypen dict
# 3. 'addresses["Bella"]' retunerar Bella's addres
# 4. 'addresses["Daniel"] = "Prinsgränd 2"' lägger till Daniel i dict'en med addresen 'Prinsgränd 2'
# 5. 'len(addresses)' retunerar hur många keys det finns i 'addresses'
#   5.1 se kommentar
#   5.2 se kommentar
# 6. 'cars' har datatypen list
# 7. cars[X] retunerar 'Opel' eftersom vi har satt X=1 och 'Opel' är på index 1 i 'cars'
# 8. cars[Y] retunerar 'IndexError: list index out of range' eftersom vi har satt Y=4 och 'cars' bara har tree items
# 9. cars[0] retunerar 'BMW' efter som cars.sort() sorterar listan 'cars' i bokstavsordning
# 10. 'cars_2 = cars' kopierar inte inehållet i 'cars' till 'cars_2', utan 'cars_2' blir en referenc till 'cars'
# 11. 'numbers1' och 'numbers2' har datatypen set
# 12. 'numbers1' har värdena 1, 2, 3, 6. 'numbers2' har värdena 2,3,4,7
# 13. snittet mellan 'numbers1' och 'numbers2' är 2, 3
# 14. unionen mellan 'numbers1' och 'numbers2' är 1, 2, 3, 4, 6, 7
# 15. den symmetriska differensen mellan numbers1 och numbers2 är 1, 4, 6, 7