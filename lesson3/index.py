#create a set using curly braskets

#my_set= {1,2,3}
#print(my_set)

#creating a set form a list using the set() function
#my_set = ([4,5,6])
#print(my_set)

#create a empty set using the set() function
#my_set = {1,1,2,2,3,3,4,4,5,3,2,3}
#print(my_set)



###########################

set1 = {1,2,3}
set2 = {3,4,5}

#union
union_method = set1.union(set2)
print("the union between set1 and set2 is:",union_method)

#operator
union_operator = set2 | set2
print("the union between set1 and set2 using operator is:",union_operator)

# Intersection
intersection_method = set1.intersection(set2)
print("The intersection between set1 and set2 is:", intersection_method)

# Operator
intersection_operator = set1 & set2
print("The intersection between set1 and set2 using operator is:", intersection_operator)

# Difference
difference_method = set1.difference(set2)
print("The difference between set1 and set2 is:", difference_method)

# Operator
difference_operator = set1 - set2
print("The difference between set1 and set2 using operator is:", difference_operator)

# Symmetric Difference
symmetric_difference_method = set1.symmetric_difference(set2)
print("The symmetric difference between set1 and set2 is:", symmetric_difference_method)

# Operator
symmetric_difference_operator = set1 ^ set2
print("The symmetric difference between set1 and set2 using operator is:", symmetric_difference_operator)


# S E T - M E T H O D S
#create a set
my_set = {1,2,3}

#add a number
my_set.add(7)

#remove
my_set.remove(3)
#discard
my_set.discard(8)
print(my_set)
#removing
my_set.clear()
print(my_set)

#duplications form a list
#create a list
my_list = [1,2,2,2,3,4,4,4,5,6]
#convert this list to a set to remove duplications
unique_set = set(my_list)
print(unique_set)

#convert set to alist
unique_list = list(unique_set)
print(unique_list)

#cheking fo common elements
blertas_interest = {"music","movies","travel"}
drilonis_interest = {"movies","games","it work"}


common_intests = blertas_interest.intersection(drilonis_interest)
print(common_intests)


#in operator

colors = {"red","green","orange"}
color = "blue"
print(color in colors)
