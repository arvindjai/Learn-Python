# Classes and Object
# concept of self

class Person:
    name = "Arvind"
    occupation = "Engineer"
    age = 30
    def info(self):
        print(f"{self.name} is an {self.occupation} with age {self.age}")

a = Person()  # Created object a of class Person
a.name = "Nausheen"
a.occupation = "Accountant"
a.age = 25

b = Person()  # Created object b of class Person
b.name = "Talib"
b.occupation = "Mechanic"
b.age = 28

a.info()
b.info()
Person.info(Person)
# Person.info(a)
# Person.info(b)
# Person.info(Person)

''' Instead of writing the below print statement again & again, 
we can create method and call #class.method(obj)'''
# print(f"{a.name} is an {a.occupation} with age {a.age}")
# print(f"{Person.name} is an {Person.occupation} with age {Person.age}")
# print(f"{b.name} is a {b.occupation} with age {b.age}")
