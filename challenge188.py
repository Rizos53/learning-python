available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

empty_list = []
current_choice = None

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        # print(f"Adding {chosen_part}")
        if current_choice in empty_list:
            # it's already in, so remove it.
            print(f"Removing {chosen_part}")
            empty_list.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            empty_list[current_choice] = chosen_part
        print(f"Your list now contains: {empty_list}")
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
