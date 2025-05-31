# class Studeni:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
# studenti1 = Studeni("drilon", 16)
# print("name:", studenti1.get_name())
# studenti1.set_name("s1mple")
# print("updated name:", studenti1.get_name())
#
# print("age", studenti1.get_age())
# studenti1.set_age(17)
# print("updated age:", studenti1.get_age())

class animal:
    def sound(self):
        print("make animal sound")
class dog(animal):
    def sound(self):
        print("ham ham")
class cat(animal):
    def sound(self):
        print("meow meow")
animal1 = animal()
animal.sound()

dog1 = dog()
dog.sound()

cat1 = cat()
cat.sound()