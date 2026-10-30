class animal:  #parent class/ supper class/ base class
    isMammal = True
    age = 3


    def movement(self):
        print("Animal is moving")

class dog(animal):    #
    def bark(self):
        print("Woof woof")

class cat(animal):
    def meow(self):
        print("Meow meow")

dog1 = dog()
dog1.bark()

cat1 = cat()
cat1.meow()

print(dog1.age, dog1.isMammal)

#assigmnet  polymophism


