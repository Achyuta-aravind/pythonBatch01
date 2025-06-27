
# 🧠 Python Modules – Complete Tutorial

## 🔸 What is a Module?

A **module** is simply a `.py` file containing Python code — functions, classes, or variables — which can be reused in other Python scripts.

## 🔹 1. Why Use Modules?

✅ Code reusability  
✅ Logical separation of concerns  
✅ Makes large projects manageable  
✅ Many pre-built (standard and 3rd-party) modules

## 🔹 2. Types of Modules

1. **Built-in modules** – Come with Python  
   e.g., `math`, `os`, `datetime`, `random`
2. **User-defined modules** – You create them yourself  
   e.g., `my_module.py`
3. **Third-party modules** – Installed via `pip`  
   e.g., `numpy`, `pandas`, `flask`

## 🔹 3. Creating & Using a Module

### Create `my_module.py`:
```python
def add(a, b):
    return a + b

def greet(name):
    print(f"Hello, {name}!")
```

### Use in another file:
```python
import my_module

result = my_module.add(2, 3)
my_module.greet("Achyuta")
```

## 🔹 4. Import Variants

### a. Import Entire Module
```python
import math
print(math.sqrt(16))
```

### b. Import Specific Functions
```python
from math import sqrt
print(sqrt(25))
```

### c. Import with Alias
```python
import math as m
print(m.ceil(3.2))
```

### d. Wildcard Import (Not Recommended)
```python
from math import *
print(sin(pi/2))
```

## 🔹 5. Module Search Path
Python looks for modules in:
1. Current directory
2. PYTHONPATH (env variable)
3. Standard library
4. `site-packages` (for installed packages)

Check module path:
```python
import sys
print(sys.path)
```

## 🔹 6. `__name__ == "__main__"`

```python
# my_module.py
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()
```

## 🔹 7. Built-in Modules (Examples)

### `math` module:
```python
import math
print(math.pi)
print(math.factorial(5))
```

### `random` module:
```python
import random
print(random.randint(1, 10))
```

### `datetime` module:
```python
from datetime import datetime
print(datetime.now())
```

### `os` module:
```python
import os
print(os.getcwd())
```

## 🔹 8. Installing Third-Party Modules with pip

```bash
pip install numpy
```

```python
import numpy as np
print(np.array([1, 2, 3]))
```

## 🔹 9. Package vs Module

- **Module** = Single `.py` file  
- **Package** = Folder with multiple modules and a special `__init__.py`

```
my_package/
├── __init__.py
├── module1.py
└── module2.py
```

Usage:
```python
from my_package import module1
```

## ✅ Summary Table

| Concept                    | Example                                |
|----------------------------|----------------------------------------|
| Import module              | `import math`                          |
| From-import                | `from math import sqrt`                |
| Aliased import             | `import pandas as pd`                  |
| User-defined module        | `import my_module`                     |
| Third-party module install | `pip install requests`                 |
| Module search path         | `import sys; print(sys.path)`          |
| Conditional execution      | `if __name__ == "__main__":`           |

## 🧪 Practice Tasks

1. Create a module with arithmetic functions  
2. Import it into another script and use it  
3. Use `os` and `datetime` modules to create timestamped folders  
4. Install and use a third-party module like `requests`
