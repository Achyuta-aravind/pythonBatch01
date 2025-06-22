# 📘 Python Dictionaries - Complete Guide

## 📖 What is a Dictionary?

A **dictionary** is an unordered, mutable, and indexed collection of **key-value pairs**.

```python
my_dict = {"name": "Alice", "age": 25}
```

## 🔑 Key Features

| Feature                   | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| **Mutable**               | You can change, add, or remove items after creation      |
| **Unordered**             | In Python < 3.7, no guaranteed order (ordered from 3.7+) |
| **Key-value pairs**       | Each item has a unique key and a value                   |
| **Keys must be hashable** | (e.g., int, str, tuple — not list/dict)                  |
| **Fast lookup**           | Dictionaries use hashing → very efficient                |

### 🧬 Dictionary Syntax
### ✅ Creating a Dictionary
```
person = {
    "name": "John",
    "age": 30,
    "location": "India"
}
```

### ✅ Using dict() Constructor

```
person = dict(name="John", age=30)
```

### 📚 Accessing & Modifying
### 🔍 Access Values

```
print(person["name"])              # John
print(person.get("age"))           # 30
print(person.get("salary", "NA"))  # NA (default fallback)
```

### ✍️ Modify/Add Values

```
person["age"] = 35
person["email"] = "john@example.com"
```

### ❌ Remove Items

```
del person["age"]
person.pop("location")
person.clear()  # Removes all items
```
### 🔁 Looping Through a Dictionary

```
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

for value in person.values():
    print(value)
```

### 🛠️ Dictionary Methods

```
Method	Description
.get(key)	Returns value or None / default
.keys()	Returns all keys
.values()	Returns all values
.items()	Returns list of (key, value) tuples
.update(dict2)	Adds or updates key-value pairs
.pop(key)	Removes key and returns its value
.clear()	Removes all items
.setdefault()	Adds key with default if not present
.copy()	Returns shallow copy
fromkeys(keys)	Creates dict from list of keys
```

```
new_dict = dict.fromkeys(["a", "b", "c"], 0)
# {'a': 0, 'b': 0, 'c': 0}
```

### 🔗 Nested Dictionaries

```
students = {
    "s1": {"name": "Alice", "marks": 90},
    "s2": {"name": "Bob", "marks": 85}
}
print(students["s1"]["name"])  # Alice
```

### 📊 Dictionary Comprehension

```
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### ✅ Dictionary vs List

```
Feature	Dictionary	List
Access	By key	By index
Structure	Key-value	Ordered elements
Mutability	Mutable	Mutable
Lookup speed	Faster (O(1))	Slower (O(n))
```

#### ⚠️ Dictionary Keys Must Be:
Unique

#### Immutable (e.g., str, int, tuple)
#### ❌ No list or dict as keys

### 🧠 Advanced Use Cases

```
1. Using Tuple as Key
locations = {("lat", "long"): "Hyderabad"}
2. Counting with collections.Counter

from collections import Counter
count = Counter("banana")
```

```
# Counter({'a': 3, 'n': 2, 'b': 1})
💡 Real-Life Example
product = {
    "id": 101,
    "name": "Phone",
    "price": 9999,
    "tags": ["electronics", "mobile"]
}
```

### ✅ Summary

```
Dictionaries store data in key-value pairs.

They are mutable and support efficient lookup.

Ideal for structured data, configs, JSON, etc.
```
