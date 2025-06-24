import copy

# Plain list (no nested lists)
original = [[1, 2],[3, 4]]

# Shallow and deep copies
#shallow = copy.copy(original)
#deep = copy.deepcopy(original)

# Modify the original list
original[0][0] = 99

#print("Original:", original)
#print("Shallow Copy:", shallow)
#print("Deep Copy:", deep)
