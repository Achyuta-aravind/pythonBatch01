#text-format data we will use strings datatype and its in quotations
# packages
import math #built-in package



# Functional approach or class based approach

name = "Arjun" #variable declaration


print() #built-in function

# string is group of characters letters, symbols, digits but inside quotations
print("You are coder!!",name)
print(type(name))

sin = 'single quotes'

dou = "double quotes"

tri = """ triple quotes """

trip = ''' triple quotes'''

'''
This is the program which is 
for automating processes
'''


#n = "TV is on, "raju""
#n = "TV is on, 'raju'"
n = 'TV is on, "raju"'
print(n)
print(type(trip))

# Indexing, Slicing
language = "Telugu"
print(language)

# Concatination
print("Vinay"+language)
print(language[0])
print(language[-1])
print(language[0:2]) #slicing

print(language.find("gu")) #built-in method
print(type(language)) #built-in function

#string is group of characters
name1 = "Varshini"
print(len(name1))
print(name1[0])
print(name1[0:])
print(name1[0:4])
print(name1[0:6:2])

#String Operations
first_name = "Ajay "
last_name = "Bhoopati"
num = 9
print(first_name+last_name) #string concatination

print(first_name*4) #repetition
print(9*4)

print('V' in name1) #membership
print(first_name==last_name) #comparison
print(first_name<last_name)

for char in first_name:
    print(char)

for char in first_name:
    print(char,end="*")

print(first_name.find('j'))
print(first_name.index("A"))
print(first_name.startswith("A"))
print(first_name.endswith("y"))

f_name =" Pramod Kumar"
print(f_name)
print(f_name.strip())
print(f_name.lstrip())
print(f_name.rstrip())

print(f_name.replace("P","R"))
print(f_name.split())
print(f_name.split('d'))

email="abc2345@gmail.com"
print(email)
print(email.split("@"))

piece = email.split("@")
print(piece[1].split("."))

print("-".join(["A", "B"])) #delimiter


print("ABV \nXYZ")

print("ABV\tXYZ")

print("abcda\\nger")
print("Pitta's")