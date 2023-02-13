# 1. Create new empty dictionary
# 2. Iterate over the keys and values of the dictionary that's being copied.
# 3. For each key, copy the value, then add the copy of the value to the new dictionary.
# 4. Your function only has to handle values that are dictionaries or lists. Both of those objects
#    have a copy method.

animals = {
    "lion": ["scary", "scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# Perform a shallow copy
things = animals.copy()

# Perform a deep copy
# things = copy.deepcopy(animals)

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])