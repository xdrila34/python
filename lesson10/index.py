from abc import ABC, abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
# class Square(shape):
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length * self.length
#
# circle = Circle(7)
# square = Square(10)
#
# print(circle.area())
# print(square.area())
class Printable(ABC):

        @abstractmethod
         def print_info(self):
            pass
class Book(Printable):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def print_info(self):
        print(f"Book: {self.title} by {self.author}")

book = Book()
book. print_info()


#

# class Studeni:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
# studenti1 = Studeni("drilon", 16)
# print("name:", studenti1.get_name())
# studenti1.set_name("s1mple")
# print("updated name:", studenti1.get_name())
#
# print("age", studenti1.get_age())
# studenti1.set_age(17)
# print("updated age:", studenti1.get_age())