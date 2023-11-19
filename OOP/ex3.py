# Parameterized Constructor in python

class Person:
    def __init__(self, n, o):
        print("Welcome")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Arvind","IT Engineer")  #Paramater passing
b = Person("Rituraj", "Hadoop Admin")
# a.name = "Arvind"
# a.occ = "Engineer"
a.info()
b.info()
