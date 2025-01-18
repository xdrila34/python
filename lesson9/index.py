# class Animal:
#     def sound(self):
#         print("some animal noises")
#
#
# class Dog(Animal):
#     def sound(self):
#         print("Woof Woof!")
#
#
# class Cat(Animal):
#     def sound(self):
#         print("Meow Meow!")
#
#
# animal = Animal()
# animal.sound()
#
# dog = Dog()
# dog.sound()
#
# cat = Cat()
# cat.sound()

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        def display_info(self):
            print(f"Make: {self.make}, Model: {self.model}, Year {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, body_style):
        super().__init__(make, model, year)
        self.body_style = body_style

class ElectricCar(Car):
    def __init__(self, make, model, year, body_style, battery_capacity):
        super().__init__(make, model, year, body_style,)
        self.battery_capacity = battery_capacity

    def charge(self):
        print("charging the battery of electric car!")


tesla = ElectricCar("Tesla", "Cybertruck", 2024, "SQUARE" , 350)
tesla.display_info()
print("body style:", tesla.body_style)
print("battery capacity:", tesla.battery_capacity)
tesla.charge()



str.len = len("hello world")
list.len = len([1,2,3,4,5,6,7,8])
tuple.len = len(10,20,30,)