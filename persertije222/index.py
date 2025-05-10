


class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"hi my name is {self.name}")

p1 = Person("drilon")
p1.greet()

class Rectangle:
     def __init__(self, width, length):
         self.width = width
         self.length = length
     def area(self):
         return self.width * self.length

sr = Rectangle(6,9)
print(sr.area())

class Pet:
    def __init__(self, name, age, species, breed, color):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.color = color
    def pet_name(self):
        print(f"the pets name is {self.name}")
    def pet_age(self):
        print(f"the age of the pet is {self.age}")
    def pet_species(self):
        print(f"the species of the pet is {self.species}")
    def pet_breed(self):
        print(f"the breed of the pet is {self.breed}")
    def pet_color(self):
        print(f"the color of the pet is {self.color}")
dog = Pet("dog",5,"dog","bulldog","brown")
dog.pet_name()
dog.pet_age()
dog.pet_species()
dog.pet_breed()
dog.pet_color()