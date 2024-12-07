#int -> str
age = 16

age_as_str = str(age)
print(age_as_str, "type of", type(age_as_str))



#int -> boolean
print(bool(0))
print(bool(43))

print(bool(""))
print(bool("hello"))

print(bool([]))
#print(bool(none))


#int + double
x = 85
y = 9.5
result = x + y
print(result, "type of ", type(result))

age = 16
message = "iam " + str(age) + " years old"
print(message)

a = 5
b = "3"
message2 = a * int(b)
print(message2)