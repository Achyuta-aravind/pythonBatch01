# 🐍 Python Sets - Complete Tutorial

A **set** is an **unordered**, **mutable**, and **unindexed** collection of **unique elements** in Python.

---

## 📌 Creating Sets

```python
# Empty set
empty_set = set()

# Set with elements
my_set = {1, 2, 3, 4}

# From a list
set_from_list = set([1, 2, 2, 3])  # {1, 2, 3}
```

❌ Duplicates Not Allowed
```
nums = {1, 2, 2, 3}
print(nums)  # Output: {1, 2, 3}
```


🔁 Accessing and Looping
# No indexing (like lists), must loop
for item in my_set:
    print(item)
    
✅ Check Membership
print(2 in my_set)  # True
print(5 not in my_set)  # True

➕ Adding Elements
my_set.add(5)
➖ Removing Elements
my_set.remove(3)      # Raises error if not present
my_set.discard(10)    # Does nothing if not present


📤 Set Operations
```
1. Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)         # {1, 2, 3, 4, 5}
print(a.union(b))    # Same
2. Intersection
print(a & b)            # {3}
print(a.intersection(b))
3. Difference
print(a - b)            # {1, 2}
print(a.difference(b))
4. Symmetric Difference
print(a ^ b)            # {1, 2, 4, 5}
print(a.symmetric_difference(b))
```

🔍 Set Methods Summary

```
Method	Description
add(elem)	Add an element
remove(elem)	Remove element (error if not found)
discard(elem)	Remove element if exists
pop()	Remove and return random item
clear()	Remove all elements
copy()	Shallow copy of the set
union(set)	Return union
intersection(set)	Return intersection
difference(set)	Return difference
symmetric_difference(set)	Return symmetric difference
issubset(set)	Check if subset
issuperset(set)	Check if superset
isdisjoint(set)	Check if no elements in common
```


✅ Set Comparisons
```
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))     # True
print(b.issuperset(a))   # True

🧠 Frozenset
```
Immutable version of a set:
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # Error!
```

📘 Real-World Use Cases

```
1. Removing duplicates from a list
emails = ["a@example.com", "b@example.com", "a@example.com"]
unique_emails = set(emails)  # {'a@example.com', 'b@example.com'}
2. Comparing users' preferences
likes_tea = {"Alice", "Bob"}
likes_coffee = {"Bob", "Charlie"}
print(likes_tea & likes_coffee)  # {'Bob'}
```

🎯 When to Use Sets
When you need unique items
When performing mathematical set operations
When checking membership efficiently (faster than lists)
✅ Sets are fast, simple, and perfect for many real-world tasks involving unique data or comparisons.
