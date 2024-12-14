#from logging import exception

try:
    result = 10/10
    print(result)
except ZeroDivisionError:
     error = "the number you are trying to devdie a number with 0"
     print(error)

fruits = {
    "apple": 4,
    "cherry": 3,
    "banana": 5

}
try:
    print(fruits["banana"])
except KeyError:
    print("the fruit is not on the dictionary")



text = ("this is a string")

try:
    print(int(text))

except Exception as e:
    print("there was an error while prasing the data ", e)



try:
    number =  10/3
except:
    print("the number you are trying to devide is not alivabile right now")
else:
    print("the devision  has gone sucessufuly  congrats and the result is: ", number)

try:
    number2 = 10/2

except ZeroDivisionError:
    print("cannot be devided ")
finally:
    print("the number has finally been devided")