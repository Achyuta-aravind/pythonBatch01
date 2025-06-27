# sets are unordered order cannot be preserved

# Empty set
empty_set = set()


# Set with elements
my_set = {1, 2, 3, 4} # will not have the fixed memory space at run time
print(my_set)
#print(my_set[0])
fs = fronzenset(my_set)
print(type(fs))


# From a list
set_from_list = set([1, 2, 2, 3])  # {1, 2, 3}

# set have no duplications
my_list = [1, 2, 2, 3]
print(my_list)
set2 = set(my_list)
print(set2)

# example

#dmart
#cooking

appliance = {"spoons","cookers","bowls","others","banana"}
print(appliance)
#fruits
fruits = {'apple', 'orange', 'strawberry',"banana"}
print(fruits)

# union of both cart
cart = appliance.union(fruits)
print(cart)

print(appliance.intersection(fruits))

fruits.discard('cherry')
print(fruits)


fruits.discard('orange')
print(fruits)

