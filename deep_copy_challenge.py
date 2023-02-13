# 1. Create new empty dictionary
# 2. Iterate over the keys and values of the dictionary that's being copied.
# 3. For each key, copy the value, then add the copy of the value to the new dictionary.
# 4. Your function only has to handle values that are dictionaries or lists. Both of those objects
#    have a copy method.
animals = {
    "deer": ["fast", "agile", "thin"],
    "bear": ["big", "strong", "brown"],
    "shark": ["fish", "flexible", "sea-creature"]
}

def my_deepcopy(d: dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values aren't
    lists or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values of copies of the original values.
    """

    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict



my_deepcopy(animals)
animals_copy = my_deepcopy(animals)
print(animals_copy["deer"]["fast"])
print(animals_copy["deer"]["fast"])