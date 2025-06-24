# The data which no need to change at given time
from django.contrib.auth import authenticate

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)

print(tuple1)

#one method to declare tuple
tuple_var = 1,2 #packing
print("values in tuples", tuple_var)
# unpacking



print(type(tuple_var))

t = (5,6,7,8,9)
print("type of t", type(t))

print(t[1])     # 20
print(t[-1])    # 40
print(t[1:3])   # (20, 30)

print(tuple1+tuple2) #concatination
print(tuple1[0]+tuple2[0]) #addition of two elements in different tuples
print(tuple1*2) #repetition
print(tuple1[0]*2) #Multiplication

# Membership operators in, not in
print(1 not in tuple2)



for item in tuple1:
    print(item)


# Aadhar
# user should not change his/her aadhar details
# if they want to change, need authentication

tuple4 = ("sreenivas", "varshini", "Archana")
del tuple4[0]
print(tuple4)
authentication_done = bool(input("Place your finger on the screen ..."))
for index in range(len(tuple4)):
    print(tuple4[index])
    if authentication_done == True:
        list4 = list(tuple4)




