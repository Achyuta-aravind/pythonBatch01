# Tuples

## 🧱 What is a Tuple in Python?
A tuple is an immutable, ordered collection of items. Tuples are similar to lists, but once created, their elements cannot be changed, added, or removed.

### 🧬 Tuple Syntax
```
# Creating a tuple
t = (1, 2, 3)
print(type(t))  # <class 'tuple'>
```

```
# Single element tuple (must include a comma)
t1 = (5,)       # Correct
t2 = (5)        # Not a tuple, just an int
```

### ✅ Key Properties of Tuples

```
Property	Description
Ordered	Items have a defined order
Immutable	Cannot be changed after creation
Heterogeneous	Can contain different data types
Indexable	Supports indexing and slicing
Hashable	Can be used as dictionary keys (if elements are also hashable)
```
### 📚 Tuple Operations

```
1. Indexing & Slicing
t = (10, 20, 30, 40)
print(t[1])     # 20
print(t[-1])    # 40
print(t[1:3])   # (20, 30)
2. Concatenation & Repetition
a = (1, 2)
b = (3, 4)
print(a + b)      # (1, 2, 3, 4)
print(a * 2)      # (1, 2, 1, 2)
3. Membership
t = (1, 2, 3)
print(2 in t)     # True
4. Iteration
for item in (1, 2, 3):
    print(item)
🔧 Tuple Methods
Tuples support only two built-in methods:
t = (1, 2, 2, 3)
print(t.count(2))     # 2
print(t.index(3))     # 3
```

### 🧠 When to Use Tuples

```
When you want to protect data from being changed

For fixed collections (e.g., coordinates, RGB colors)

As keys in dictionaries

For returning multiple values from functions
def get_position():
    return (10, 20)

x, y = get_position()
```

### 🧊 Tuple Packing and Unpacking

```
# Packing
point = 10, 20

# Unpacking
x, y = point
# Extended unpacking
a, *b, c = (1, 2, 3, 4, 5)
# a = 1, b = [2, 3, 4], c = 5
```

### 🔄 Mutable Elements Inside Tuples
Tuples are immutable, but they can contain mutable objects like lists:
```
t = (1, 2, [3, 4])
t[2][0] = 99
print(t)  # (1, 2, [99, 4])
```

### 🛠️ Performance & Memory
```
Tuples are more memory-efficient and faster than lists due to their immutability.
Use tuples for read-only or fixed-size data.
🧪 Tuple vs List: Quick Comparison
Feature	Tuple	List
Mutability	Immutable	Mutable
Syntax	( )	[ ]
Speed	Faster	Slower
Memory usage	Less	More
Built-in Methods	Fewer	Many
```
```
📌 Example: Using Tuple as Dictionary Key
location = {}
key = (12.34, 56.78)
location[key] = "Some Place"
print(location[(12.34, 56.78)])
```
