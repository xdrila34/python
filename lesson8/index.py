#def calculate_area(length, width):
    #
#return length + width
#def calculate_perimeter(length, width):
    #return 2 * (length + width)

#length = 5
#width = 6

#area = calculate_area(length, width)
#perimeter = calculate_perimeter(length, width)

#print(f"area, {area}")
#print(f"perimeter, {perimeter}")

#class Rectangle:
    #def __init__(self, length, width):
        #self.length = length
        #self.width = width
    #def calculate_area(self):
       # return self.length + self.width
    #def calulate_perimeter(self):
        #return 2 * (self.length +self.width)

#my_rectangle = Rectangle(2,3)
#area = my_rectangle.calculate_area()
#perimeter = my_rectangle.calulate_perimeter()
#print(f"area: {area}")
#print(f"perimeter: {perimeter}")

class njeri:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hello, iam {self.name}, and i am {self.age} years old")

person1 = njeri("drilon", 16)
person2 = njeri("yll", 17)
print(person1)
print(person2)