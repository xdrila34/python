

number1 = 10
number2 = 12
operator = '+'
if operator == '+':
    result = number1 + number2
    print("you are trying to add the numbers", result)
elif operator == '-':
    result2 = number1 - number2
    print("you are trying to subtract the numbers", result2)
else:
    raise ValueError("you are trying to do something thats not really posible on our end")

#userinput = input("enter to numbers ")

#print(float(userinput))

arithmetic = input("give me a number")
arithmetic2 = input("give me a second number")

arithmeticresult = int(arithmetic) + int(arithmetic2)
try:
    print("ive added the numbers for you and it resulted to ", arithmeticresult)

except ValueError:
    print("the numbers you gave me are not usable ")
except:
    print("something is not right")
finally:
    print(arithmeticresult)