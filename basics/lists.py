#numbers
num = 45
num1 = 45.75
num2 = 45+75j

#Strings
char = 'B'
name = "Birla"

#Lists
collection_of_names = ["Birla", "Cinthya", "Damodar"] #Square brace

collection_of_different_items = ["Soap", "Shampoo", 30, 50, True, 45.5] #Square brace
# Heterogeneous


# Example
my_list = [1, 2, 3, 'apple', True, 4.5]
print(my_list)
print(my_list[0])
print(my_list[5])
print(my_list[-1])
#print(my_list[6]) #IndexError

#no elements
empty_list = []
print(empty_list)

# Facebook
friends_list = []
print(friends_list)

#nested list
nes_list = [[1,2],[3,4]]
print(nes_list)
print(nes_list[0])
print(nes_list[0][0])


#slicing
my_list1 = [1, 2, 3, 'apple', True, 4.5]
print(my_list1[0:3])

# for loop
for item in my_list1:
    print(item)


# for loop
for item in my_list1:
    if item == 'apple':
        break
    print(item)

# for loop
for item in my_list1:
    if type(item) == str:
        break
    print(item)


# Facebook
friends_list = []
friends_list.append('ismart_shankar')
print(friends_list)

# Request acceptance, Request
for i in range(0,3):
   friends_list.append('fanboy{}'.format(i))

print(friends_list)


my_list = [3,7, 2, 3]
my_list.append(4)            # Adds to end
my_list.insert(1, 1.5)       # Inserts at index
my_list.extend([5, 6])
print(my_list)# Adds multiple elements

my_list.remove(3)      # Removes first occurrence of 3
print(my_list)# Adds multiple elements
my_list.pop(1)   # Removes item at index 1
print(my_list)# Adds multiple elements
del my_list[0]         # Deletes item at index 0
print(my_list)# Adds multiple elements


#sorting
nums = [5, 2, 9, 1]
nums1 = nums.copy()
#shallow copy
nums1[0]=78
print(nums1)
print(nums)

squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

# List comprehensions
squares1 = [x**2 for x in range(1,10)]
print(squares1)

print(len(squares1)) #length of the list
print(min(squares1))
print(max(squares1))
print(sum(squares1))



squares1.append(23)
print(squares1)

squares1.insert(1,14)
print(squares1)

squares1 = squares1.index(14)
print(squares1)


names = ['arjun', 'amith']
f_scores = [90, 80]

paired = list(zip(names,f_scores))  # [('a', 90), ('b', 80)]
print(paired)

a,b,c = 1,2,3
print(a,b,c)

a,b,c = [4,5,6]
print(a,b,c)