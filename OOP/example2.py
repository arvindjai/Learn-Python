# Default Constructor in python

class Person:
    def __init__(self):
        print("Welcome")
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person()
b = Person()
a.name = "Arvind"
a.occ = "Engineer"
a.info()
