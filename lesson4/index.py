#create a list

names = ["drilon","eros","blinera","blerta"]

#omterate in the naems lst and print evry name

for name in names:
    print(name)

###########################

sentance = "whats up!"
for charachter in sentance:
    if charachter.isalpha(): #chek if the charter is a letter
        print(charachter)

# range funcition

for number in range (1,6):
    print(number)
###########################


numbers = [12,45,6,72,21,8,94,57]
#initilaze a variable "maximum" with th first value from the list numbers
maximum = numbers[0]

for num in numbers: #begin a loop interating through each element in the list of "numbers"
    if num > maximum: #chek if the current eelement "num" is bigger then the current maximum value
        maximum = num #if so, update the maximum value to the current element in num
        print("the highest value on the list is ", maximum)


######################################################
   # while loop
count = 1 # initilize the loop control variable
while count <= 5: # the contion if count is less then or equal to 5
    print("iteration",count)
    count += 1 # increment the loop control variable

######################################################
# do while loop
# infinite loop
while True:

    user_input  = input("enter a positive number: ")
#chek if the input is a numberic
    if user_input is numeric:
         number = int(user_input)

            if number > 0:
             break

        #print the error message for invalid input
        #print the error message for invalid input
        print("invalid input please try again")
    #print the valid positive number entereed by the user
             print("you have entered a valid positive number:",number)






