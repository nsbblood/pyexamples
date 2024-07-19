class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Using polymorphism
animals = [Dog(), Cat()]  ##

for animal in animals:
    animal.sound() 
