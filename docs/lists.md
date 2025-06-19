# Lists in python

## Definition
A list is a collection of ordered, mutable, and indexable items in Python. Lists can hold items of any data type, including other lists.

```
# Example
my_list = [1, 2, 3, 'apple', True, 4.5]
```
### Creating Lists
```
# Empty list
empty_list = []

# List with elements
numbers = [10, 20, 30, 40]

# Mixed data types
mixed = [1, "hello", 3.14, False]

# Nested lists
nested = [[1, 2], [3, 4]]

```
### Accessing Elements
```
my_list = ['a', 'b', 'c', 'd']

print(my_list[0])    # 'a'
print(my_list[-1])   # 'd' (last element)
```
### Slicing Lists
```
my_list = ['a', 'b', 'c', 'd', 'e']

print(my_list[1:4])     # ['b', 'c', 'd']
print(my_list[:3])      # ['a', 'b', 'c']
print(my_list[::2])     # ['a', 'c', 'e']

```


### Looping Through Lists
```
for item in my_list:
    print(item)

# With index
for i in range(len(my_list)):
    print(i, my_list[i])

```
### Adding Elements
```
my_list = [1, 2, 3]

my_list.append(4)            # Adds to end
my_list.insert(1, 1.5)       # Inserts at index
my_list.extend([5, 6])       # Adds multiple elements

```
### Removing Elements
```
my_list = [1, 2, 3, 4, 5]

my_list.remove(3)      # Removes first occurrence of 3
my_list.pop()          # Removes last item
my_list.pop(1)         # Removes item at index 1
del my_list[0]         # Deletes item at index 0
```
### Searching in Lists
```
my_list = [1, 2, 3, 4, 5]

print(3 in my_list)            # True
print(my_list.index(4))        # 3
print(my_list.count(2))        # 1
```

### Sorting and Reversing
```
nums = [5, 2, 9, 1]

nums.sort()            # In-place ascending
nums.sort(reverse=True)
print(sorted(nums))    # Returns new sorted list

nums.reverse()         # Reverses list in-place
```
### Clearing and Copying
```
nums = [1, 2, 3]
copy_nums = nums.copy()  # Shallow copy

nums.clear()              # Empties the list
```

### List comprehension
```
squares = [x**2 for x in range(5)]
even = [x for x in range(10) if x % 2 == 0]
```

### List functions and Methods
```
| Function / Method  | Description                       |
| ------------------ | --------------------------------- |
| `len(lst)`         | Returns number of elements        |
| `min(lst)`         | Smallest item                     |
| `max(lst)`         | Largest item                      |
| `sum(lst)`         | Sum of elements (numeric only)    |
| `list(iterable)`   | Converts iterable to list         |
| `lst.append(x)`    | Adds element to end               |
| `lst.insert(i, x)` | Inserts element at index          |
| `lst.extend(iter)` | Adds all elements from iterable   |
| `lst.remove(x)`    | Removes first occurrence          |
| `lst.pop([i])`     | Removes and returns item at index |
| `lst.clear()`      | Empties the list                  |
| `lst.index(x)`     | Finds index of first occurrence   |
| `lst.count(x)`     | Counts occurrences                |
| `lst.sort()`       | Sorts list in-place               |
| `lst.reverse()`    | Reverses list in-place            |
| `lst.copy()`       | Returns a shallow copy            |
```

## Advanced Topics

### Nested List Access
```
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3
```

### Using zip() with Lists
```
names = ['a', 'b']
scores = [90, 80]
paired = list(zip(names, scores))  # [('a', 90), ('b', 80)]
```

### Unpacking Lists
```
a, b, c = [1, 2, 3]
```
### Flattening Lists
```
nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]
```

### Real world usecase
```
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 90}
]

names = [student["name"] for student in students]
high_scores = [s["score"] for s in students if s["score"] > 80]
```


