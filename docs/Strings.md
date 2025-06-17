# Strings in python

## Description

Topics to Learn: Strings Datatype, Operations, flow control statements, I/O operations, CRUD operations

## Agenda
- Strings
- Indexing/Slicing
- Operations
- Flowcontrol statements
- I/O Operations
- CRUD Operations


```Pycharm
# Definition 
	s1 = "Hello"
	s2 = 'World'
	s3 = """Multi-line
string
"""

```


```Pycharm
# Indexing and slicing
	s = "Python"
	print(s[0])     # P (indexing starts at 0)
	print(s[-1])    # n (negative indexing)
	print(s[1:4])   # yth (slicing)
  print(len(s))   # 6

```

```
# String Operations
Operation	Syntax	Example Result
Concatenation	s1 + s2	"Hello" + "World" → "HelloWorld"
Repetition	s * 3	"Hi" * 3 → "HiHiHi"
Membership	'a' in s	True or False
Comparison	s1 == s2, s1 > s2	Lexicographical
Iteration	for ch in s:	Iterate characters
```

```
s.find("th")          # returns index or -1
s.index("th")         # like find, but raises error if not found
s.startswith("Py")
s.endswith("on")
```

```
#Case Handling
s.upper()
s.lower()
s.capitalize()
s.title()
s.swapcase()

```

```
#Trimming
s.strip()             # removes whitespace
s.lstrip()
s.rstrip()
```

```
#Replace and Split
s.replace("Py", "My")   # replace substrings
s.split(" ")            # split into list by delimiter
",".join(["A", "B"])    # join list into string
```

```
#Count and Tests
	s.count("o")           # how many times 'o' appears
	s.isalpha()            # only letters?
	s.isdigit()            # only digits?
	s.isalnum()            # alphanumeric?
	s.isspace()            # only whitespace?
```

```
#String Formatting
  f-Strings (Recommended)
	name = "Alice"
	age = 30
	print(f"My name is {name} and I am {age} years old.")
```

```
#format() Method
	print("My name is {} and I am {} years old.".format(name, age))
  % Formatting (Old Style)
	print("My name is %s and I am %d years old." % (name, age))

#Multiline Strings
text = """This is
a multi-line
string."""
```

```
#Looping through Strings

for char in "Python":
    print(char)

#Escape Characters
	Escape	Meaning
	\n	New line
	\t	Tab
	\\	Backslash
	\'	Single quote
	\"	Double quote
```

```
#Raw Strings
	Useful for regex or Windows paths:
	path = r"C:\Users\Name\Folder"
```

---

## Finally
- **Exercises**: Reverse string without built-in function.
- **Usage**: Build prompt interface to get details and process them.
- **Interview Questions**: 

---
