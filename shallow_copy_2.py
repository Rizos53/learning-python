teddy_list = ["cuddly", "stuffed"]
elephant_list = ["big", "grey", "wrinkled"]
lion_list = ["scary", "scary", "big", "cat"]

animals = {
    "lion": ["scary", "scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# things = animals.copy()
things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

print(things["teddy"])
print(animals["teddy"])

print()

# things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)