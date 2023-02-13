available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
cart = {}

while current_choice != "0":

    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        cart[current_choice] = available_parts[current_choice]
        print(f"adding {chosen_part}")

    else:
        print("Please add options from the list: ")
        for key, value in available_parts.items():
            print(f"{key}: {value}")

    print("Current items in cart: ")
    print(cart)

    current_choice = input("> ")