available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
added_items = {}
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"adding {chosen_part}")
        for added_items in current_choice:
            current_choice += added_items
            print(f"Added items: {added_items}")

    else:
        print("Please add options from the list: ")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")