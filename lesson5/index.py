

total = 0
for number in range(1,11):
    if number % 2 == 0:
     total += number
print("shuma e numrave qift prej 1-10 eshte:", total)

def greet():
    print("hello world!!")

greet()

def greet_person(name):
    print("hello", name)

greet_person("filan")

 #result = add(3,8)
 #print ("3+7 =", result)

greeting = "hello"

def greet(name):
     message = f"{greeting}, {name}!"
     print(message)
greet("michael")
print(greeting)

#default args
def greet_person(name, greeting="hello"):
    message = f"{greeting}, {name}"
    return message
default_greeting = greet_person("drilon")
costom_greeting = greet_person("eris","hi")
print(default_greeting+)
print(costom_greeting)