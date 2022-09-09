firstname = "john"
lastname = "smith"
tele = "00468123456789"
fullname = "john smith"

print(len(fullname), len(firstname), len(lastname))
print(firstname, lastname, tele)
print(fullname + "\n" + tele)
print(f'{fullname}\n{tele}')
print('{} {}\n{}'.format(firstname, lastname, tele))
print('A name %s' % firstname)