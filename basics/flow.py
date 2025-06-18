"""
Definition:
"""

# line-by-line execution
age = 17

# if elif else block
if age >= 18:
    print("Hello you are",age)

elif age <= 10: #else-if
    print("Go to school dont involve in politics")

else:
    print("no statment executed")

#nested if
if age > 0:
    if age >= 18:
        print("Hello you are", age)

    elif age <= 10:  # else-if
        print("Go to school dont involve in politics")

    else:
        print("no statment executed")



for age in range(0,3): #0 1 2 n-1 n=3
    print("vin")

age = 0 #initialize
while age <5: #condition should be false at certainpoint
    print(age) #block of code
    age += 3 #Increment