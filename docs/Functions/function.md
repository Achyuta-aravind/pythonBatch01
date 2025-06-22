# 📘 Python Functions – A Complete Overview
Functions in Python are blocks of reusable code that perform a specific task. They help you avoid repetition, make code cleaner, and improve readability.

### ✅ Why Use Functions?
Modularity – Break complex problems into smaller pieces.

Reusability – Write once, use many times.

Maintainability – Easier to fix/update.

Readability – Code is easier to understand.

### 📌 Basic Syntax
def function_name(parameters):
    # code block
    return result
    
### 🔹 Example
def greet(name):
    return f"Hello, {name}!"
print(greet("Achyuta"))

### 🧩 Types of Functions

#### Type	Description
- Built-in Functions	Predefined in Python (len(), print(), type())
- User-defined Functions	Created by users using def
- Lambda Functions	Anonymous functions using lambda keyword
- Recursive Functions	Functions that call themselves

### 🛠️ Function Arguments
```
Positional Arguments
def add(a, b):
    return a + b

```
Keyword Arguments
def greet(name, msg):
    print(f"{msg}, {name}")
greet(name="Achyuta", msg="Welcome")

```
Default Arguments
def greet(name, msg="Hello"):
    print(f"{msg}, {name}")
```

```
Variable-Length Arguments
*args for non-keyword variable args
def total(*numbers):
    return sum(numbers)
```

```
**kwargs for keyword variable args
def show_details(**info):
    print(info)
```
 
### ♻️ Return Statement
```
def multiply(x, y):
    return x * y
result = multiply(3, 5)
print(result)
```

### 🧠 Lambda (Anonymous) Functions

```
square = lambda x: x * x
print(square(5))  # Output: 25
```

### 🔄 Recursive Function

```
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```
    
### 🧪 Function Scope
- Local Scope – Inside a function
- Global Scope – Outside all functions
- global Keyword – To modify global variables inside a function

### 🎯 Example: Real Use Case

```
def is_even(num):
    return num % 2 == 0
even_numbers = list(filter(is_even, range(10)))
print(even_numbers)  # Output: [0, 2, 4, 6, 8]
```
