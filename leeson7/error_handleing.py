try:
    result = 10/10

except:
    print("the reslut is not ")

fruits = {
    "apple": 4,
    "pear": 3,
    "banana": 5

}
try:
    print(fruits[input("tell me a fruits")])
except KeyError:
    print("the fruit is not on the dictionary")


