#class is a blue print of an object
#object is an instance of a class
from collections.abc import async_generator
from os import name


class employee:
    def __init__(self, name, position, age, gender):
        self.name = name
        self.position = position
        self.age = age
        self.gender = gender



    def drive(self):
        print("employee is driving")

    def eat(self):
        print("employee is eating")



employee1 = employee("Jospeh", "senior Developer", 22, "male")
employee2 = employee("edith", "junior devloper", 20, "female")
employee3 = employee("msoo", "learner", 19, "female")


print("name:", employee1.name, employee1.age, employee1.gender, employee1.position)
employee1.drive()

