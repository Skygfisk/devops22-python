class Person:
    def __init__(self):
        self.street = "Kummelbyvägen"
        self.street_number = 16
        self.post_code = 19143
        self.country = "Sverige"

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.employee_number = 1137
        self.salary = 28000

class Address:
    def __init__(self):
        self.street = "Apelgatan"
        self.street_number = 5
        self.post_code = 75435
        self.country = "Uppsala"

class Student:
    def __init__(self, address):
        self.address = address
        self.employee_number = 2201
        self.salary = 0

me = Student(Address())
print(me.address.post_code)