#definition: datatypes: what kind of the data you are storing (type of data)
# Datatype: Numbers

# Integer type
num1 = 10
num2 = -20
print(num1, num2)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
# Float type
num3 = 999.99
print(num3 / num2)
# Complex type
# 1+2i mathematically
comp = 2j
print(comp)
comp = 3+2j
print(comp)
# Expressions
# e=mc2
m,c = 2,1
e = m*c**2
print(e)
# operators
salary1 = 7800
salary2 = 2200
print(salary1, salary2)
# Arithmetic operators
print(salary1+salary2)
print(salary1-salary2)
print(salary1*salary2)
print(salary1/salary2)
print(salary1//salary2)
print(salary1%salary2)
# assignment operators
x = 10
x+=1
print(x)
# operators: num1, num2 these are the operands and + or -, ...etc.
# same memory
x = 10
y = 10
#print memory address
print(id(x),id(y))
z = 10
print(id(z))

# built-in functions
# doing some task


# type conversion, you convert one data type into another
# datatype
gh = 89
print(gh)
print(type(gh))
print(float(gh)) # integer to float

flo = 3.14
print(int(flo)) # float into integer

e = 1789
print(e)
print(bin(e))
print(hex(e)) # 0-9 + a-f
print(oct(e)) # upto 7, 0-7

#var_name = data
account_num = 106749
account_balance = 12300.67
print(type(account_num),type(account_balance))


# Immutability
a = 168
print(id(a))
a = 169
print(id(a))
