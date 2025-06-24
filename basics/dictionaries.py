new_list = [1,2,3,4]

new_dict = {"name1":"Varshini", "name2":"Archana"}
print(type(new_dict))

# dictionary syntax key:value

#new_dict1 = {[1,2,3,4]:"Varshini", "name2":"Archana"}

new_dict1 = {"Varshini":[1,2,3,4], "name2":"Archana"}
print(new_dict1)


person = {
    "name": "Archana",
    "age": 20,
    "location": "Anantapur"
}
print(person)
print(dict(name1="Sreeni", age=26))


# Accessing values
print(person["name"])
print(person["age"])
print(person["location"])


# can you modify

person["name"] = "Taara"
person["location"] = "hyderabad"
print(person)

#remove values
del person["name"]
print(person)

# pop method
person.pop("age")
print(person)
#Entire dictionary will be removed
person.clear()
print(person)


# for loop for list

for item in new_list:
    print(item)


# for loop for dictionary
new_dict3 = {"name1":"Varshini", "name2":"Archana"}

# only the keys
for item in new_dict3:
    print(item)


#key value both will extract by items()
for item in new_dict3.items():
    print(item)

for key,value in new_dict3.items():
    print(key,"*****",value)


# methods
print(new_dict3.items())
print(new_dict3.get("name2"))
print(new_dict3.keys())
print(new_dict3.values())

print(new_dict3.pop("name2"))
print(new_dict3.items())

dict4 = new_dict3.copy()
print(dict4)


new_dict = dict.fromkeys(["a", "b", "c"], 0)
# {'a': 0, 'b': 0, 'c': 0}
print(new_dict)

# Nested dictionaries
students = {
    "s1": {"name": "Alice", "marks": 90,"address":{"location":"Tirupati"}},
    "s2": {"name": "Bob", "marks": 85}
}
print(students["s1"]["name"])  # Alice
print(students["s2"]["name"])
print(students["s1"]["address"]["location"])


#comprehension

squares = {}
for x in range(5):
    square = x ** 2
    squares[x] = square
print(squares)

squares = {x:x**2 for x in range(5)}
print(squares)

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

